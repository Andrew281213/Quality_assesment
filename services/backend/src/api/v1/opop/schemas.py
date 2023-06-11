from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Opop


OpopPublic = pydantic_model_creator(
	Opop, name="OpopPublic"
)

OpopCreate = pydantic_model_creator(
	Opop, name="OpopCreate", include=("program_code", "direction_code", "profile_title", "start_year")
)

OpopUpdate = pydantic_model_creator(
	Opop, name="OpopUpdate", include=("program_code", "direction_code", "profile_title", "start_year")
)
