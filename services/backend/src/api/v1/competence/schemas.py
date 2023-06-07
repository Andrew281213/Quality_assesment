from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Competence


CompetencePublic = pydantic_model_creator(
	Competence, name="CompetencePublic", include=("id", "title")
)

CompetenceCreate = pydantic_model_creator(
	Competence, name="CompetenceCreate", include=("title",)
)

CompetenceUpdate = pydantic_model_creator(
	Competence, name="CompetenceUpdate", include=("title",)
)
