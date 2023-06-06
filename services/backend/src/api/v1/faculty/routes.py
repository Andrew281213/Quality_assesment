from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Faculty
from .schemas import FacultyCreate, FacultyPublic, FacultyUpdate

faculty_router = APIRouter()


@faculty_router.get("/", response_model=list[FacultyPublic])
async def get_faculties():
	return await Faculty.all()


@faculty_router.get("/{faculty_id}", response_model=FacultyPublic)
async def get_faculty(faculty_id: int):
	try:
		return await Faculty.get(id=faculty_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Факультет не найден"
		)


@faculty_router.post("/", response_model=FacultyPublic)
async def create_faculty(faculty: FacultyCreate):
	faculty_dict = faculty.dict(exclude_unset=True)
	try:
		return await Faculty.create(**faculty_dict)
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такой факультет уже существует"
		)


@faculty_router.put("/{faculty_id}")
async def update_faculty(faculty_id: int, new_data: FacultyUpdate):
	faculty = Faculty.get_or_none(id=faculty_id)
	if faculty is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Факультет не найден"
		)
	await Faculty.filter(id=faculty_id).update(**new_data.dict())
	return {"message": "Данные успешно обновлены"}


@faculty_router.delete("/{faculty_id}")
async def delete_faculty(faculty_id: int):
	faculty = Faculty.get_or_none(id=faculty_id)
	if faculty is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Факультет не найден"
		)
	await Faculty.filter(id=faculty_id).delete()
	return {"message": "Факультет успешно удален"}
