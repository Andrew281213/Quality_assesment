from tortoise import fields, models


class Group(models.Model):
	id = fields.IntField(pk=True, index=True)
	full_title = fields.CharField(max_length=128, unique=True, null=False, description="Полное наименование группы")
	short_title = fields.CharField(max_length=32, unique=True, description="Краткое наименование группы")
	faculty = fields.ForeignKeyField("models.Faculty", related_name="groups")

	class PydanticMeta:
		exclude = ("study_plans",)
		allow_cycles = False
		max_recursion = 1
