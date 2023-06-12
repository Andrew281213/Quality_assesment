from tortoise import fields, models


class Opop(models.Model):
	id = fields.IntField(pk=True, index=True)
	code = fields.CharField(max_length=64, unique=True, null=False, index=True, description="Шифр программы")
	title = fields.CharField(max_length=128, null=False, description="Название профиля")
	start_year = fields.IntField(description="Год начала программы")
	direction = fields.ForeignKeyField("models.Direction", "opop")

	class PydanticMeta:
		exclude = ("disciplines",)
