from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import IntegrityError, DoesNotExist

from .models import StudyPlan, StudyPlanDiscipline
from .schemas import StudyPlanCreate, StudyPlanPublic, StudyPlanUpdate, StudyPlanDisciplinePublic, \
	StudyPlanDisciplineCreate
from ..group.models import Group

study_plan_router = APIRouter()


async def check_group(idx: int):
	if await Group.get_or_none(id=idx) is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такая группа не найдена"
		)


async def check_study_plan(idx: int):
	if await StudyPlan.get_or_none(id=idx) is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой план не найден"
		)


@study_plan_router.get("/", response_model=list[StudyPlanPublic])
async def get_study_plans():
	return await StudyPlanPublic.from_queryset(StudyPlan.all())


@study_plan_router.get("/{study_plan_id}", response_model=StudyPlanPublic)
async def get_study_plan(study_plan_id: int):
	try:
		return await StudyPlan.get(id=study_plan_id).prefetch_related("group")
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Учебный план не найден"
		)


@study_plan_router.post("/", response_model=StudyPlanPublic)
async def create_study_plan(study_plan: StudyPlanCreate):
	await check_group(study_plan.group_id)
	study_plan_dict = study_plan.dict(exclude_unset=True)
	try:
		res = await StudyPlan.create(**study_plan_dict)
		return await StudyPlanPublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такой учебный план уже существует"
		)


@study_plan_router.put("/{study_plan_id}")
async def update_study_plan(study_plan_id: int, new_data: StudyPlanUpdate):
	await check_group(new_data.group_id)
	if await StudyPlan.get_or_none(id=study_plan_id) is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Учебный план не найден"
		)
	await StudyPlan.filter(id=study_plan_id).update(**new_data.dict())
	return {"message": "Данные успешно обновлены"}


@study_plan_router.delete("/{study_plan_id}")
async def delete_study_plan(study_plan_id: int):
	study_plan = await StudyPlan.get_or_none(id=study_plan_id)
	if study_plan is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Учебный план не найден"
		)
	await StudyPlan.filter(id=study_plan_id).delete()
	return {"message": f"Учебный план {study_plan.title} успешно удален"}


@study_plan_router.get("/{study_plan_id}/disciplines", response_model=list[StudyPlanDisciplinePublic])
async def get_study_disciplines(study_plan_id: int):
	return await StudyPlanDisciplinePublic.from_queryset(StudyPlanDiscipline.filter(study_plan=study_plan_id).all())


@study_plan_router.post("/{study_plan_id}/", response_model=StudyPlanDisciplinePublic)
async def create_study_discipline(study_plan_id: int, study_discipline: StudyPlanDisciplineCreate):
	await check_study_plan(study_plan_id)
	study_discipline_dict = study_discipline.dict(exclude_unset=True)
	try:
		res = await StudyPlanDiscipline.create(study_plan_id=study_plan_id, **study_discipline_dict)
		return await StudyPlanDisciplinePublic.from_tortoise_orm(res)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Такая дисциплина уже добавлена"
		)


# TODO: put & delete to study_plan_discipline
