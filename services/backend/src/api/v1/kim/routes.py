from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Kim, KimApplicability
from ..competence.routes import _get_competence_discipline
from .schemas import KimPublic, KimUpdate, KimCreate, KimApplicabilityPublic, KimApplicabilityCreate

kim_router = APIRouter()


async def check_kim(kim_id: int):
	if await Kim.get_or_none(id=kim_id) is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой ким не существует"
		)


@kim_router.get("/", response_model=list[KimPublic])
async def get_kims():
	return await Kim.all()


@kim_router.get("/{kim_id}", response_model=KimPublic)
async def get_kim(kim_id: int):
	try:
		return await Kim.get(id=kim_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Ким не найден"
		)


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


@kim_router.get("/{kim_id}/applicability", response_model=list[KimApplicabilityPublic])
async def get_applicabilities(kim_id: int):
	await check_kim(kim_id)
	res = KimApplicability.filter(kim_id=kim_id).all()
	return await KimApplicabilityPublic.from_queryset(res)


@kim_router.post("/{kim_id}/applicability/", response_model=KimApplicabilityPublic)
async def create_applicability(kim_id: int, kim_applicability: KimApplicabilityCreate):
	await check_kim(kim_id)
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
