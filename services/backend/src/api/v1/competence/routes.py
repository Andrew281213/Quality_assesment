from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Competence
from .schemas import CompetencePublic, CompetenceUpdate, CompetenceCreate

competence_router = APIRouter()


@competence_router.get("/", response_model=list[CompetencePublic])
async def get_competencies():
	return await Competence.all()


@competence_router.post("/", response_model=CompetencePublic)
async def create_competence(competence: CompetenceCreate):
	competence_dict = competence.dict(exclude_unset=True)
	try:
		return await Competence.create(**competence_dict)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая компетенция уже существует"
		)


@competence_router.get("/{competence_id}", response_model=CompetencePublic)
async def get_competence(competence_id: int):
	try:
		return await Competence.get(id=competence_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой компетенции не существует"
		)


# TODO: put & delete methods
