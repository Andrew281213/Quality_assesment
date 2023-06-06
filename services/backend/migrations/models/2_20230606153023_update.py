from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "group" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "full_title" VARCHAR(128) NOT NULL UNIQUE,
    "short_title" VARCHAR(32) NOT NULL UNIQUE,
    "faculty_id" INT NOT NULL REFERENCES "faculty" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "group"."full_title" IS 'Полное наименование группы';
COMMENT ON COLUMN "group"."short_title" IS 'Краткое наименование группы';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "group";"""
