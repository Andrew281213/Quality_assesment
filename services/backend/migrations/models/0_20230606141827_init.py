from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "faculty" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "full_title" VARCHAR(128) NOT NULL UNIQUE,
    "short_title" VARCHAR(64)  UNIQUE
);
COMMENT ON COLUMN "faculty"."full_title" IS 'Полное наименование факультета';
COMMENT ON COLUMN "faculty"."short_title" IS 'Сокращенное наименование факультета';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
