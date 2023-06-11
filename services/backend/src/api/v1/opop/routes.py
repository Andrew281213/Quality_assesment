from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Opop
from ..direction.models import Direction
from .schemas import OpopCreate, OpopPublic, OpopUpdate

opop_router = APIRouter()


async def check_direction(idx: int):
	if await Direction.get_or_none(id=idx) is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такое направление не найдено"
		)


@opop_router.get("/", response_model=list[OpopPublic])
async def get_opops():
	res = Opop.all()
	return await OpopPublic.from_queryset(res)


@opop_router.post("/", response_model=OpopPublic)
async def create_opop(opop: OpopCreate):
	opop_dict = opop.dict()
	await check_direction(opop.direction_id)
	try:
		res = await Opop.create(**opop_dict)
		return await OpopPublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такой профиль уже существует"
		)


@opop_router.get("/{opop_id}", response_model=OpopPublic)
async def get_opop(opop_id: int):
	try:
		return OpopPublic.from_tortoise_orm(Opop.get(id=opop_id))
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой профиль не найден"
		)


@opop_router.put("/{opop_id}", response_model=OpopPublic)
async def update_opop(opop_id: int, opop: OpopUpdate):
	opop_dict = opop.dict()
	opop = await Opop.get_or_none(id=opop_id)
	if opop is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой профиль не найден"
		)
	await Opop.filter(id=opop_id).update(**opop_dict)
	return await OpopPublic.from_tortoise_orm(Opop.get(id=opop_id))


@opop_router.delete("/{opop_id}")
async def update_opop(opop_id: int):
	opop = await Opop.get_or_none(id=opop_id)
	if opop is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой профиль не найден"
		)
	await Opop.filter(id=opop_id).delete()
	return {"msg": f"Профиль {opop.title} успешно удален"}
