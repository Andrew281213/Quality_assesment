from fastapi import APIRouter

from .v1.discipline.routes import discipline_router
from .v1.competence.routes import competence_router
from .v1.kim.routes import kim_router


router = APIRouter()
router.include_router(discipline_router, prefix="/v1/discipline", tags=["discipline"])
router.include_router(competence_router, prefix="/v1/competence", tags=["competence"])
router.include_router(kim_router, prefix="/v1/kim", tags=["kim"])
