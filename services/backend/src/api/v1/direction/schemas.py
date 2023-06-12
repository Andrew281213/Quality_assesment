from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Direction
from tortoise import Tortoise
from src.database.config import TORTOISE_ORM

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")

DirectionPublic = pydantic_model_creator(
	Direction, name="DirectionPublic", include=("id", "code", "title")
)

DirectionCreate = pydantic_model_creator(
	Direction, name="DirectionCreate", include=("code", "title")
)

DirectionUpdate = pydantic_model_creator(
	Direction, name="DirectionUpdate", include=("code", "title")
)
