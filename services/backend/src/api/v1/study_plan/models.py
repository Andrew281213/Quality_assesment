from tortoise import fields, models


class StudyPlan(models.Model):
	id = fields.IntField(pk=True, index=True)
	group_id = fields.ForeignKeyField("models.Group", "")