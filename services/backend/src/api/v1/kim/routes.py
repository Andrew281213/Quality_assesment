from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Kim, KimApplicability
from ..dcs.routes import _get_competence_discipline
from .schemas import KimPublic, KimUpdate, KimCreate, KimApplicabilityPublic, KimApplicabilityCreate

kim_router = APIRouter()


async def _get_kim(kim_id: int):
	res = await Kim.get_or_none(id=kim_id)
	if res is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой ким не существует"
		)
	return res


@kim_router.get("/", response_model=list[KimPublic])
async def get_kims():
	res = Kim.all()
	return await KimPublic.from_queryset(res)


@kim_router.get("/{kim_id}", response_model=KimPublic)
async def get_kim(kim_id: int):
	return await KimPublic.from_tortoise_orm(await _get_kim(kim_id))


@kim_router.post("/", response_model=KimPublic)
async def create_kim(kim: KimCreate):
	kim_dict = kim.dict(exclude_unset=True)
	try:
		return await Kim.create(**kim_dict)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такой ким уже существует"
		)


@kim_router.put("/{kim_id}")
async def update_kim(kim_id: int, new_data: KimCreate):
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


@kim_router.get("/{kim_id}/applicability", response_model=list[KimApplicabilityPublic])
async def get_applicabilities(kim_id: int):
	await _get_kim(kim_id)
	res = KimApplicability.filter(kim_id=kim_id).all()
	return await KimApplicabilityPublic.from_queryset(res)


@kim_router.post("/{kim_id}/applicability/", response_model=KimApplicabilityPublic)
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


# TODO: put & delete methods for kim & kim applicability
