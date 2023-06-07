from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Faculty

FacultyCreate = pydantic_model_creator(
	Faculty, name="FacultyCreate", exclude=("id",)
)

FacultyUpdate = pydantic_model_creator(
	Faculty, name="FacultyUpdate", exclude=("id",)
)

FacultyPublic = pydantic_model_creator(
	Faculty, name="FacultyPublic", include=("id", "full_title", "short_title"),
)
