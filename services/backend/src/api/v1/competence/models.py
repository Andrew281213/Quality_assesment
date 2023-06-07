from tortoise import fields, models


class Competence(models.Model):
	id = fields.IntField(pk=True, index=True)
	title = fields.CharField(max_length=128, unique=True, null=False)
