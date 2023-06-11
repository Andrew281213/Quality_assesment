from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Direction
from .schemas import DirectionPublic, DirectionCreate, DirectionUpdate

direction_router = APIRouter()


@direction_router.get("/", response_model=list[DirectionPublic])
async def get_directions():
	return await Direction.all()


@direction_router.get("/{direction_id}", response_model=DirectionPublic)
async def get_direction(direction_id: int):
	try:
		return await Direction.get(id=direction_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Направление не найдено"
		)


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
