from tortoise import fields, models


class Discipline(models.Model):
	id = fields.IntField(pk=True, index=True)
	code = fields.CharField(max_length=64, unique=True, description="Шифр дисциплины")
	title = fields.CharField(max_length=128, null=False, description="Наименование дисциплины")
	end_semester = fields.IntField(null=False, description="Последний семестр")
	program = fields.ForeignKeyField("models.Opop", "disciplines")

	class PydanticMeta:
		exclude = ("kim_applicability", "discipline_competence", "program.competencies")
