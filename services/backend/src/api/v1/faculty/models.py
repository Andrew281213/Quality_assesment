from tortoise import fields, models
from tortoise.exceptions import NoValuesFetched


class Faculty(models.Model):
	id = fields.IntField(pk=True, index=True)
	full_title = fields.CharField(max_length=128, unique=True, null=False, description="Полное наименование факультета")
	short_title = fields.CharField(max_length=64, unique=True, null=True, description="Сокращенное наименование факультета")
