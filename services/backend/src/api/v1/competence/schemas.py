from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Competence, DisciplineCompetence
from tortoise import Tortoise
from src.database.config import TORTOISE_ORM

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")


CompetencePublic = pydantic_model_creator(
	Competence, name="CompetencePublic", exclude=("opop.direction",)
)

CompetenceCreate = pydantic_model_creator(
	Competence, name="CompetenceCreate", include=("code", "title", "type", "opop_id")
)

CompetenceUpdate = pydantic_model_creator(
	Competence, name="CompetenceUpdate", include=("code", "title", "type", "opop_id")
)

DisciplinePublic = pydantic_model_creator(
	DisciplineCompetence, name="DisciplineCompetencePublic",
	exclude=("competence.opop", "discipline.program", "kim_applicability.kim")
)

DisciplineCreate = pydantic_model_creator(
	DisciplineCompetence, name="DisciplineCompetenceCreate", include=("discipline_id",)
)

DisciplineUpdate = pydantic_model_creator(
	DisciplineCompetence, name="DisciplineCompetenceUpdate", include=("discipline_id",)
)
