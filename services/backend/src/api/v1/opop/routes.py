from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Opop
from ..direction.routes import _get_direction
from .schemas import OpopCreate, OpopPublic, OpopUpdate

opop_router = APIRouter()


async def _get_opop(idx: int):
	res = await Opop.get_or_none(id=idx)
	if res is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой профиль не найден"
		)
	return res


@opop_router.get("/", response_model=list[OpopPublic])
async def get_opops():
	res = Opop.all()
	return await OpopPublic.from_queryset(res)


@opop_router.post("/", response_model=OpopPublic)
async def create_opop(opop: OpopCreate):
	opop_dict = opop.dict()
	await _get_direction(opop.direction_id)
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
	return await OpopPublic.from_tortoise_orm(await _get_opop(opop_id))


@opop_router.put("/{opop_id}", response_model=OpopPublic)
async def update_opop(opop_id: int, opop: OpopUpdate):
	opop_dict = opop.dict()
	await _get_opop(opop_id)
	try:
		await Opop.filter(id=opop_id).update(**opop_dict)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такой профиль уже существует"
		)
	return await OpopPublic.from_tortoise_orm(await Opop.get(id=opop_id))


@opop_router.delete("/{opop_id}")
async def delete_opop(opop_id: int):
	opop = await _get_opop(opop_id)
	await Opop.filter(id=opop_id).delete()
	return {"msg": f"Профиль {opop.title} успешно удален"}
