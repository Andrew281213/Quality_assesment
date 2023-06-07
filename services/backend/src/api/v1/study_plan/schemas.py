from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.config import TORTOISE_ORM
from .models import StudyPlan, StudyPlanDiscipline

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")

StudyPlanPublic = pydantic_model_creator(
	StudyPlan, name="StudyPlanPublic"
)

StudyPlanCreate = pydantic_model_creator(
	StudyPlan, name="StudyPlanCreate", include=("title", "group_id")
)

StudyPlanUpdate = pydantic_model_creator(
	StudyPlan, name="StudyPlanUpdate", include=("title", "group_id")
)

StudyPlanDisciplinePublic = pydantic_model_creator(
	StudyPlanDiscipline, name="StudyPlanDisciplinePublic"
)

StudyPlanDisciplineCreate = pydantic_model_creator(
	StudyPlanDiscipline, name="StudyPlanDisciplineCreate", include=("discipline_id", "hours", "semester")
)
