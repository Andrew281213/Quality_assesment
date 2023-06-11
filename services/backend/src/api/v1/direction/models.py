from tortoise import fields, models


class Direction(models.Model):
	id = fields.IntField(pk=True, index=True)
	direction_code = fields.CharField(max_length=64, null=False, unique=True, description="Шифр направления")
	title = fields.CharField(max_length=128, null=False, description="Название направления")
