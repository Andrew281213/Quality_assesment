from tortoise import fields, models


class StudyPlan(models.Model):
	id = fields.IntField(pk=True, index=True)
	title = fields.CharField(max_length=128, null=False, unique=True)
	group = fields.ForeignKeyField("models.Group", "study_plans")
	created_at = fields.DatetimeField(auto_now_add=True)

	class PydanticMeta:
		exclude = ("study_plan_disciplines",)
		allow_cycles = False
		max_recursion = 1


class StudyPlanDiscipline(models.Model):
	study_plan = fields.ForeignKeyField("models.StudyPlan", "study_plan_disciplines")
	discipline = fields.ForeignKeyField("models.Discipline", "study_plan_disciplines")
	hours = fields.IntField(null=False)
	semester = fields.IntField(null=False)

	class Meta:
		unique_together = (("study_plan", "discipline", "semester"),)

	class PydanticMeta:
		exclude = ("study_plan", "study_plan_id")
		allow_cycles = False
		max_recursion = 1
