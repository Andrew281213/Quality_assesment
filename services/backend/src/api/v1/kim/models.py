from tortoise import fields, models


class Kim(models.Model):
	id = fields.IntField(pk=True, index=True)
	text = fields.CharField(max_length=255, null=False, unique=True)
	img = fields.CharField(max_length=255, null=True)

	class PydanticMeta:
		pass
		# exclude = ("kim_applicability", )


class KimApplicability(models.Model):
	id = fields.IntField(pk=True, index=True)
	kim = fields.ForeignKeyField("models.Kim", "kim_applicability")
	discipline_competence = fields.ForeignKeyField("models.DisciplineCompetence", "kim_applicability")

	class Meta:
		unique_together = ("kim", "discipline_competence")
		ordering = ("id",)
