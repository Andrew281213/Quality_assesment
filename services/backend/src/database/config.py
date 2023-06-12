import os
from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"models": {
			"models": [
				"src.api.v1.direction.models",
				"src.api.v1.opop.models", "src.api.v1.competence.models", "src.api.v1.kim.models",
				"src.api.v1.discipline.models", "aerich.models"
			],
			"default_connection": "default"
		}
	}
}
