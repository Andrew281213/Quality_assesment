from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Group
from .schemas import GroupCreate, GroupPublic, GroupUpdate
from ..faculty.models import Faculty

group_router = APIRouter()


async def check_faculty(idx):
	if await Faculty.get_or_none(id=idx) is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой факультет не найден"
		)


@group_router.get("/", response_model=list[GroupPublic])
async def get_groups():
	return await GroupPublic.from_queryset(Group.all())


@group_router.get("/{group_id}", response_model=GroupPublic)
async def get_group(group_id: int):
	try:
		return await Group.get(id=group_id).prefetch_related("faculty")
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Группа не найдена"
		)


@group_router.post("/", response_model=GroupPublic)
async def create_group(group: GroupCreate):
	await check_faculty(group.faculty_id)
	group_dict = group.dict(exclude_unset=True)
	try:
		res = await Group.create(**group_dict)
		return await GroupPublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая группа уже существует"
		)


@group_router.put("/{group_id}")
async def update_group(group_id: int, new_data: GroupUpdate):
	await check_faculty(new_data.faculty_id)
	group = await Group.get_or_none(id=group_id)
	if group is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Группа не найдена"
		)
	await Group.filter(id=group_id).update(**new_data.dict())
	return {"message": "Данные успешно обновлены"}


@group_router.delete("/{group_id}")
async def delete_group(group_id: int):
	group = await Group.get_or_none(id=group_id)
	if group is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Группа не найдена"
		)
	await Group.filter(id=group_id).delete()
	return {"message": f"Группа {group.full_title} успешно удалена"}
