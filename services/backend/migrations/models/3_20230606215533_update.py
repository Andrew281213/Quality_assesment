from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "studyplan" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "group_id_id" INT NOT NULL REFERENCES "group" ("id") ON DELETE CASCADE
);;
        CREATE TABLE IF NOT EXISTS "studyplandiscipline" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "hours" INT NOT NULL,
    "semester" INT NOT NULL,
    "discipline_id" INT NOT NULL REFERENCES "discipline" ("id") ON DELETE CASCADE,
    "study_plan_id" INT NOT NULL REFERENCES "studyplan" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "studyplan";
        DROP TABLE IF EXISTS "studyplandiscipline";"""
