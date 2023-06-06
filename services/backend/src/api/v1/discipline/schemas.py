from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Discipline


DisciplineCreate = pydantic_model_creator(
	Discipline, name="DisciplineCreate", exclude=("id",)
)

DisciplineUpdate = pydantic_model_creator(
	Discipline, name="DisciplineUpdate", exclude=("id",)
)

DisciplinePublic = pydantic_model_creator(
	Discipline, name="DisciplinePublic", include=("id", "title")
)
