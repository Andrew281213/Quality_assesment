from tortoise import fields, models


class Opop(models.Model):
	id = fields.IntField(pk=True, index=True)
	program_code = fields.CharField(max_length=64, null=False, index=True, description="Шифр программы")
	direction_code = fields.CharField(max_length=64, null=False, index=True, description="Шифр направления")
	profile_title = fields.CharField(max_length=128, null=False, description="Название профиля")
	start_year = fields.IntField(description="Год начала программы")

	class Meta:
		unique_together = ("program_code", "direction_code")
