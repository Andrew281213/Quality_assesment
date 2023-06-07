from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_studyplandi_study_p_070f3f" ON "studyplandiscipline" ("study_plan_id", "discipline_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "uid_studyplandi_study_p_070f3f";"""
