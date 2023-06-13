from fastapi import APIRouter, HTTPException, status, Query
from tortoise.exceptions import DoesNotExist, IntegrityError
from tortoise.expressions import Q
from typing import Annotated

from .models import DisciplineCompetence
from .schemas import DCCreate, DCPublic, DCUpdate

from ..competence.routes import _get_competence
from ..discipline.routes import _get_discipline


dcs_router = APIRouter()


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


@dcs_router.get("/", response_model=list[DCPublic])
async def get_dcs(
	competence_id: Annotated[int | None, Query(description="Id компетенции")] = None,
	discipline_id: Annotated[int | None, Query(description="Id дисциплины")] = None
):
	if None not in (competence_id, discipline_id):
		res = DisciplineCompetence.filter(competence_id=competence_id, discipline_id=discipline_id)
	else:
		res = DisciplineCompetence.filter(Q(competence_id=competence_id, discipline_id=discipline_id, join_type="OR")).all()
	return await DCPublic.from_queryset(res)


@dcs_router.get("/{dc_id}", response_model=DCPublic)
async def get_dc(dc_id: int):
	res = await _get_competence_discipline(idx=dc_id)
	return await DCPublic.from_tortoise_orm(res)


@dcs_router.post("/", response_model=DCPublic)
async def create_dc(dc: DCCreate):
	dc_dict = dc.dict(exclude_unset=True)
	await _get_competence(dc.competence_id)
	await _get_discipline(dc.discipline_id)
	try:
		res = await DisciplineCompetence.create(**dc_dict)
		return await DCPublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая связь дисциплины и компетенции уже существует"
		)


@dcs_router.put("/{dc_id}", response_model=DCPublic)
async def update_dc(dc_id: int, new_data: DCUpdate):
	await _get_competence_discipline(idx=dc_id)
	try:
		await DisciplineCompetence.filter(id=dc_id).update(**new_data.dict())
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая связь дисциплины и компетенции уже существует"
		)
	return await DCPublic.from_tortoise_orm(await _get_competence_discipline(idx=dc_id))


@dcs_router.delete("/{dc_id}")
async def delete_dc(dc_id: int):
	await _get_competence_discipline(idx=dc_id)
	dc = await DisciplineCompetence.get(id=dc_id).prefetch_related("discipline", "competence")
	await DisciplineCompetence.filter(id=dc_id).delete()
	return {"msg": f"Связь между {dc.discipline.title} и {dc.competence.title} успешно удалена"}
