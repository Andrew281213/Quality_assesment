from fastapi import APIRouter

from .v1.faculty.routes import faculty_router
from .v1.discipline.routes import discipline_router
from .v1.group.routes import group_router
from .v1.study_plan.routes import study_plan_router


router = APIRouter()
router.include_router(faculty_router, prefix="/v1/faculty", tags=["faculty"])
router.include_router(discipline_router, prefix="/v1/discipline", tags=["discipline"])
router.include_router(group_router, prefix="/v1/group", tags=["group"])
router.include_router(study_plan_router, prefix="/v1/study_plan", tags=["study_plan"])
