from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "competence" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(128) NOT NULL UNIQUE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "competence";"""
