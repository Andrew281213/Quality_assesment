from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Discipline
from .schemas import DisciplineCreate, DisciplineUpdate, DisciplinePublic

discipline_router = APIRouter()


@discipline_router.get("/", response_model=list[DisciplinePublic])
async def get_disciplines():
	res = Discipline.all()
	return await DisciplinePublic.from_queryset(res)


@discipline_router.get("/{discipline_id}", response_model=DisciplinePublic)
async def get_discipline(discipline_id: int):
	try:
		return await Discipline.get(id=discipline_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Дисциплина не найдена"
		)


@discipline_router.post("/", response_model=DisciplinePublic)
async def create_discipline(discipline: DisciplineCreate):
	discipline_dict = discipline.dict(exclude_unset=True)
	try:
		res = await Discipline.create(**discipline_dict)
		return await DisciplinePublic.from_tortoise_orm(res)
	except IntegrityError as e:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая дисциплина уже существует"
		)


@discipline_router.put("/{discipline_id}")
async def update_discipline(discipline_id: int, new_data: DisciplineUpdate):
	discipline = await Discipline.get_or_none(id=discipline_id)
	if discipline is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Дисциплина не найдена"
		)
	await Discipline.filter(id=discipline_id).update(**new_data.dict())
	return {"message": "Данные успешно обновлены"}


@discipline_router.delete("/{discipline_id}")
async def delete_discipline(discipline_id: int):
	discipline = await Discipline.get_or_none(id=discipline_id)
	if discipline is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Дисциплина не найдена"
		)
	await Discipline.filter(id=discipline_id).delete()
	return {"message": f"Дисциплина {discipline.title} успешно удалена"}
