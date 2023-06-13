from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Competence
from .schemas import CompetencePublic, CompetenceUpdate, CompetenceCreate

competence_router = APIRouter()


async def _get_competence(idx: int):
	competence = await Competence.get_or_none(id=idx)
	if competence is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такая компетенция не найдена"
		)
	return competence


@competence_router.get("/", response_model=list[CompetencePublic])
async def get_competencies():
	res = Competence.all()
	return await CompetencePublic.from_queryset(res)


@competence_router.post("/", response_model=CompetencePublic)
async def create_competence(competence: CompetenceCreate):
	competence_dict = competence.dict(exclude_unset=True)
	try:
		res = await Competence.create(**competence_dict)
		return await CompetencePublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая компетенция уже существует"
		)


@competence_router.get("/{competence_id}", response_model=CompetencePublic)
async def get_competence(competence_id: int):
	return await CompetencePublic.from_tortoise_orm(await _get_competence(competence_id))


@competence_router.put("/{competence_id}", response_model=CompetencePublic)
async def update_competence(competence_id: int, new_data: CompetenceUpdate):
	await _get_competence(competence_id)
	try:
		await Competence.filter(id=competence_id).update(**new_data.dict())
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая компетенция уже существует"
		)
	return await CompetencePublic.from_tortoise_orm(await Competence.get(id=competence_id))


@competence_router.delete("/{competence_id}")
async def delete_competence(competence_id: int):
	competence = await _get_competence(competence_id)
	await Competence.filter(id=competence_id).delete()
	return {"message": f"Компетенция {competence.title} успешно удалена"}
