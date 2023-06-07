from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Kim, KimApplicability


KimPublic = pydantic_model_creator(
	Kim, name="KimPublic", include=("id", "text", "img")
)

KimCreate = pydantic_model_creator(
	Kim, name="KimCreate", exclude=("id",)
)

KimUpdate = pydantic_model_creator(
	Kim, name="KimUpdate", exclude=("id",)
)

KimApplicabilityPublic = pydantic_model_creator(
	KimApplicability, name="KimApplicabilityPublic", exclude=("discipline.study_plan_disciplines",)
)

KimApplicabilityCreate = pydantic_model_creator(
	KimApplicability, name="kimApplicabilityCreate", include=("competence_id", "discipline_id")
)

KimApplicabilityUpdate = pydantic_model_creator(
	KimApplicability, name="KimApplicabilityUpdate"
)
