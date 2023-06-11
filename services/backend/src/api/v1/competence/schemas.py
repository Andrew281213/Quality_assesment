from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Competence
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
