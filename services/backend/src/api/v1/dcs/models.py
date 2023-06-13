from tortoise import fields, models


class DisciplineCompetence(models.Model):
	id = fields.IntField(pk=True, index=True)
	competence = fields.ForeignKeyField("models.Competence", "discipline_competence")
	discipline = fields.ForeignKeyField("models.Discipline", "discipline_competence")

	class Meta:
		unique_together = ("competence", "discipline")
		ordering = ("id",)

	class PydanticMeta:
		exclude = ("kim_applicability",)
