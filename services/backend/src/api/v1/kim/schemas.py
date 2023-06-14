from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Kim, KimApplicability
from tortoise import Tortoise
from src.database.config import TORTOISE_ORM

Tortoise.init_models(TORTOISE_ORM["apps"]["models"]["models"], "models")


KimPublic = pydantic_model_creator(
	Kim, name="KimPublic"
)

KimCreate = pydantic_model_creator(
	Kim, name="KimCreate", exclude=("id",)
)

KimUpdate = pydantic_model_creator(
	Kim, name="KimUpdate", exclude=("id",)
)

KimApplicabilityPublic = pydantic_model_creator(
	KimApplicability, name="KimApplicabilityPublic",
	exclude=("discipline_competence.competence.opop", "discipline_competence.discipline.program")
)

KimApplicabilityCreate = pydantic_model_creator(
	KimApplicability, name="kimApplicabilityCreate", include=("discipline_competence_id",)
)

KimApplicabilityUpdate = pydantic_model_creator(
	KimApplicability, name="KimApplicabilityUpdate", include=("discipline_competence_id",)
)
