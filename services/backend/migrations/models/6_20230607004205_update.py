from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "uid_studyplandi_study_p_070f3f";
        CREATE UNIQUE INDEX "uid_studyplandi_study_p_d3d355" ON "studyplandiscipline" ("study_plan_id", "discipline_id", "semester");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "uid_studyplandi_study_p_d3d355";
        CREATE UNIQUE INDEX "uid_studyplandi_study_p_070f3f" ON "studyplandiscipline" ("study_plan_id", "discipline_id");"""
