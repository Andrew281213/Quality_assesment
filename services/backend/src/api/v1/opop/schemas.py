from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.config import TORTOISE_ORM
from .models import Opop

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")


OpopPublic = pydantic_model_creator(
	Opop, name="OpopPublic",
)

OpopCreate = pydantic_model_creator(
	Opop, name="OpopCreate", include=("code", "title", "start_year", "direction_id")
)

OpopUpdate = pydantic_model_creator(
	Opop, name="OpopUpdate", include=("code", "title", "start_year", "direction_id")
)
