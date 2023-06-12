from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX if exists "idx_competence_title_a15d03";
        ALTER TABLE "kim" ALTER COLUMN "text" TYPE VARCHAR(255) USING "text"::VARCHAR(255);
        ALTER TABLE "kim" ALTER COLUMN "text" TYPE VARCHAR(255) USING "text"::VARCHAR(255);
        ALTER TABLE "kim" ALTER COLUMN "text" TYPE VARCHAR(255) USING "text"::VARCHAR(255);
        CREATE UNIQUE INDEX "uid_kim_text_9ad4f7" ON "kim" ("text");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_kim_text_9ad4f7";
        ALTER TABLE "kim" ALTER COLUMN "text" TYPE TEXT USING "text"::TEXT;
        ALTER TABLE "kim" ALTER COLUMN "text" TYPE TEXT USING "text"::TEXT;
        ALTER TABLE "kim" ALTER COLUMN "text" TYPE TEXT USING "text"::TEXT;
        CREATE UNIQUE INDEX "uid_competence_title_a15d03" ON "competence" ("title");"""
