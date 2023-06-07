from tortoise import fields, models


class Discipline(models.Model):
	id = fields.IntField(pk=True, index=True)
	title = fields.CharField(max_length=128, unique=True, null=False, description="Наименование дисциплины")

	class PydanticMeta:
		exclude = ("kim_applicability",)
