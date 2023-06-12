from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Competence, DisciplineCompetence
from .schemas import CompetencePublic, CompetenceUpdate, CompetenceCreate, DisciplinePublic, DisciplineCreate, \
	DisciplineUpdate
from ..discipline.routes import _get_discipline

competence_router = APIRouter()


async def _get_competence(idx: int):
	competence = await Competence.get_or_none(id=idx)
	if competence is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такая компетенция не найдена"
		)
	return competence


async def _get_competence_discipline(idx: int = None, competence_id: int = None, discipline_id: int = None):
	if idx is not None:
		res = await DisciplineCompetence.get_or_none(id=idx)
	elif competence_id is not None and discipline_id is not None:
		res = await DisciplineCompetence.get_or_none(competence_id=competence_id, discipline_id=discipline_id)
	else:
		raise ValueError("Не указаны необходимые значения")
	if res is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такая связь компетенции и дисциплины не существует"
		)
	return res


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


@competence_router.get("/{competence_id}/", response_model=list[DisciplinePublic])
async def get_dcs(competence_id: int):
	res = DisciplineCompetence.filter(competence_id=competence_id)
	return await DisciplinePublic.from_queryset(res)


@competence_router.get("/{competence_id}/{discipline_id}", response_model=DisciplinePublic)
async def get_dc(competence_id: int, discipline_id: int):
	res = await _get_competence_discipline(competence_id=competence_id, discipline_id=discipline_id)
	return await DisciplinePublic.from_tortoise_orm(res)


@competence_router.post("/{competence_id}/", response_model=DisciplinePublic)
async def create_dc(competence_id: int, dc: DisciplineCreate):
	dc_dict = dc.dict(exclude_unset=True)
	await _get_competence(competence_id)
	await _get_discipline(dc.discipline_id)
	try:
		res = await DisciplineCompetence.create(competence_id=competence_id, **dc_dict)
		return await DisciplinePublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая связь дисциплины и компетенции уже существует"
		)


@competence_router.put("/{competence_id}/{discipline_id}", response_model=DisciplinePublic)
async def update_dc(competence_id: int, discipline_id: int, new_data: DisciplineUpdate):
	await _get_competence(competence_id)
	await _get_discipline(discipline_id)
	try:
		await DisciplineCompetence.filter(competence_id=competence_id, discipline_id=discipline_id).update(**new_data.dict())
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая связь дисциплины и компетенции уже существует"
		)
	return await DisciplinePublic.from_tortoise_orm(await _get_competence_discipline(competence_id=competence_id, discipline_id=discipline_id))


@competence_router.delete("/{competence_id}/{discipline_id}")
async def delete_dc(competence_id: int, discipline_id: int):
	await _get_competence_discipline(competence_id=competence_id, discipline_id=discipline_id)
	dc = await DisciplineCompetence.get(discipline_id=discipline_id, competence_id=competence_id).prefetch_related("discipline", "competence")
	await DisciplineCompetence.filter(discipline_id=discipline_id, competence_id=competence_id).delete()
	return {"msg": f"Связь между {dc.discipline.title} и {dc.competence.title} успешно удалена"}
