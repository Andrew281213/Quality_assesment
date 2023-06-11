from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.config import TORTOISE_ORM

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")


from .models import Discipline

DisciplineCreate = pydantic_model_creator(
	Discipline, name="DisciplineCreate", include=("code", "title", "end_semester", "program_id")
)

DisciplineUpdate = pydantic_model_creator(
	Discipline, name="DisciplineUpdate", include=("code", "title", "end_semester", "program_id")
)

DisciplinePublic = pydantic_model_creator(
	Discipline, name="DisciplinePublic", exclude=("program.direction",)
)
