from tortoise.contrib.pydantic import pydantic_model_creator
from .models import DisciplineCompetence
from tortoise import Tortoise
from src.database.config import TORTOISE_ORM

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")


DCPublic = pydantic_model_creator(
	DisciplineCompetence, name="DisciplineCompetencePublic",
	exclude=("competence.opop", "discipline.program", "kim_applicability.kim")
)

DCCreate = pydantic_model_creator(
	DisciplineCompetence, name="DisciplineCompetenceCreate", include=("discipline_id", "competence_id")
)

DCUpdate = pydantic_model_creator(
	DisciplineCompetence, name="DisciplineCompetenceUpdate", include=("discipline_id", "competence_id")
)
