import asyncio

from fastapi import APIRouter, HTTPException, status, Query
from tortoise.exceptions import DoesNotExist, IntegrityError
from tortoise.expressions import Q, Subquery
from tortoise.contrib.postgres.functions import Random
from typing import Annotated

from .models import Kim, KimApplicability
from ..dcs.routes import _get_competence_discipline
from .schemas import KimPublic, KimUpdate, KimCreate, KimApplicabilityPublic, KimApplicabilityCreate
from ..dcs.models import DisciplineCompetence


kim_router = APIRouter()


async def _get_kim(kim_id: int):
	res = await Kim.get_or_none(id=kim_id)
	if res is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой ким не существует"
		)
	return res


async def _get_applicability(idx: int):
	res = await KimApplicability.get_or_none(id=idx)
	if res is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой связи кима и компетенции-дисциплины не существует"
		)
	return res


@kim_router.get("/", response_model=list[KimPublic])
async def get_kims(
	discipline_id: Annotated[int | None, Query(description="Id дисциплины")] = None,
	competence_id: Annotated[int | None, Query(description="Id компетенции")] = None
):
	if all(x is None for x in (discipline_id, competence_id)):
		res = Kim.all().distinct()
	elif None not in (discipline_id, competence_id):
		res = Kim.exclude(kim_applicability=None).filter(
			kim_applicability__discipline_competence__discipline_id=discipline_id,
			kim_applicability__discipline_competence__competence_id=competence_id
		).distinct()
	else:
		res = Kim.exclude(kim_applicability=None).filter(Q(
			kim_applicability__discipline_competence__discipline_id=discipline_id,
			kim_applicability__discipline_competence__competence_id=competence_id,
			join_type="OR"
		)).distinct()
	rand = Kim.annotate(order=Random()).order_by("order").limit(2)
	print(await KimPublic.from_queryset(rand))
	return await KimPublic.from_queryset(res)


@kim_router.get("/{kim_id}", response_model=KimPublic)
async def get_kim(kim_id: int):
	return await KimPublic.from_tortoise_orm(await _get_kim(kim_id))


@kim_router.post("/", response_model=KimPublic)
async def create_kim(kim: KimCreate):
	kim_dict = kim.dict(exclude_unset=True)
	try:
		res = await Kim.create(**kim_dict)
		return await KimPublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такой ким уже существует"
		)


@kim_router.put("/{kim_id}")
async def update_kim(kim_id: int, new_data: KimUpdate):
	await _get_kim(kim_id)
	try:
		await Kim.filter(id=kim_id).update(**new_data.dict())
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такой ким уже существует"
		)
	return {"msg": "Данные успешно обновлены"}


@kim_router.delete("/{kim_id}")
async def delete_kim(kim_id: int):
	await _get_kim(kim_id)
	await Kim.filter(id=kim_id).delete()
	return {"msg": f"Ким успешно удален"}


@kim_router.get("/applicability/", response_model=list[KimApplicabilityPublic])
async def get_applicabilities(
		kim_id: Annotated[int | None, Query(description="Id кима")] = None,
		dc_id: Annotated[int | None, Query(description="Id связи компетенции и дисциплины")] = None
):
	if all(x is None for x in (kim_id, dc_id)):
		res = KimApplicability.all()
	elif None not in (kim_id, dc_id):
		res = KimApplicability.filter(kim_id=kim_id, discipline_competence_id=dc_id).all()
	else:
		res = KimApplicability.filter(Q(kim_id=kim_id, discipline_competence_id=dc_id, join_type="OR")).all()
	return await KimApplicabilityPublic.from_queryset(res)


@kim_router.post("/applicability/", response_model=KimApplicabilityPublic)
async def create_applicability(kim_id: int, kim_applicability: KimApplicabilityCreate):
	await _get_kim(kim_id)
	kim_applicability_dict = kim_applicability.dict()
	await _get_competence_discipline(idx=kim_applicability.discipline_competence_id)
	try:
		res = await KimApplicability.create(kim_id=kim_id, **kim_applicability_dict)
		return await KimApplicabilityPublic.from_tortoise_orm(res)
	except IntegrityError as e:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая связь уже существует"
		)


@kim_router.delete("/applicability/{applicability_id}")
async def delete_applicability(applicability_id: int):
	await _get_applicability(applicability_id)
	await KimApplicability.filter(id=applicability_id).delete()
	return {"msg": "Связь кима и компетенции-дисциплины успешно удалена"}
