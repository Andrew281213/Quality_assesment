from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "discipline" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(128) NOT NULL UNIQUE
);
COMMENT ON COLUMN "discipline"."title" IS 'Наименование дисциплины';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "discipline";"""
