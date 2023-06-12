from tortoise import fields, models


class Competence(models.Model):
	id = fields.IntField(pk=True, index=True)
	code = fields.CharField(max_length=64, null=False, unique=True, description="Шифр компетенции")
	title = fields.CharField(max_length=128, null=False, description="Формулировка компетенции")
	type = fields.CharField(max_length=32, null=False, description="Тип компетенции")
	opop = fields.ForeignKeyField("models.Opop", "competencies")

	class Meta:
		ordering = ("id",)

	class PydanticMeta:
		exclude = ("kim_applicability", "discipline_competence")


class DisciplineCompetence(models.Model):
	id = fields.IntField(pk=True, index=True)
	competence = fields.ForeignKeyField("models.Competence", "discipline_competence")
	discipline = fields.ForeignKeyField("models.Discipline", "discipline_competence")

	class Meta:
		unique_together = ("competence", "discipline")
