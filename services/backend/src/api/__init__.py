from fastapi import APIRouter

from .v1.faculty.routes import faculty_router

router = APIRouter()
router.include_router(faculty_router, prefix="/v1/faculty", tags=["faculty"])
