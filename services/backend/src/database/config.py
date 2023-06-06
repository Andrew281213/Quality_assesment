import os
from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"models": {
			"models": [
				"src.api.v1.faculty.models", "aerich.models"
			],
			"default_connection": "default"
		}
	}
}