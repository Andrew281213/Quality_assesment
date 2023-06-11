from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Direction


DirectionPublic = pydantic_model_creator(
	Direction, name="DirectionPublic", include=("id", "direction_code", "title")
)

DirectionCreate = pydantic_model_creator(
	Direction, name="DirectionCreate", include=("direction_code", "title")
)

DirectionUpdate = pydantic_model_creator(
	Direction, name="DirectionUpdate", include=("direction_code", "title")
)
