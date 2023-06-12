from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Direction
from .schemas import DirectionPublic, DirectionCreate, DirectionUpdate

direction_router = APIRouter()


async def _get_direction(idx: int):
	res = await Direction.get_or_none(id=idx)
	if res is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такое направление не найдено"
		)
	return res


@direction_router.get("/", response_model=list[DirectionPublic])
async def get_directions():
	return await Direction.all()


@direction_router.get("/{direction_id}", response_model=DirectionPublic)
async def get_direction(direction_id: int):
	return await DirectionPublic.from_tortoise_orm(await _get_direction(direction_id))


@direction_router.post("/", response_model=DirectionPublic)
async def create_direction(direction: DirectionCreate):
	direction_dict = direction.dict(exclude_unset=True)
	try:
		return await Direction.create(**direction_dict)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такое направление уже существует"
		)
