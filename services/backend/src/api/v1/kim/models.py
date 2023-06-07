from tortoise import fields, models


class Kim(models.Model):
	id = fields.IntField(pk=True, index=True)
	text = fields.TextField(null=False)
	img = fields.CharField(max_length=255, null=True)

	class PydanticMeta:
		exclude = ("kim_applicability", )


class KimApplicability(models.Model):
	kim = fields.ForeignKeyField("models.Kim", "kim_applicability")
	competence = fields.ForeignKeyField("models.Competence", "kim_applicability")
	discipline = fields.ForeignKeyField("models.Discipline", "kim_applicability")

	class Meta:
		unique_together = ("kim", "competence", "discipline")
