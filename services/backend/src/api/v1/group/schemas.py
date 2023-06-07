from pydantic import BaseModel
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.config import TORTOISE_ORM
from .models import Group

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")

GroupPublic = pydantic_model_creator(
	Group, name="GroupPublic"
)

GroupCreate = pydantic_model_creator(
	Group, name="GroupCreate", include=("full_title", "short_title", "faculty_id")
)

GroupUpdate = pydantic_model_creator(
	Group, name="GroupUpdate", include=("full_title", "short_title", "faculty_id")
)


class BaseGroup(BaseModel):
	full_title: str
	short_title: str

	class Config:
		orm_mode = True

# class GroupPublic(BaseGroup):
# 	id: int
# 	faculty: FacultyPublic
#
# 	class Config:
# 		orm_mode = True


# class GroupCreate(BaseGroup):
# 	faculty_id: int


# class GroupUpdate(BaseGroup):
# 	faculty_id: int
