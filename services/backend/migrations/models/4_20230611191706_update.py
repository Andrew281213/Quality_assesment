from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "competence" ADD "code" VARCHAR(64) NOT NULL UNIQUE;
        ALTER TABLE "competence" ADD "type" VARCHAR(32) NOT NULL;
        ALTER TABLE "competence" ADD "opop_id" INT NOT NULL;
        ALTER TABLE "competence" ALTER COLUMN "title" TYPE VARCHAR(128) USING "title"::VARCHAR(128);
        CREATE UNIQUE INDEX "uid_competence_code_6cf174" ON "competence" ("code");
        ALTER TABLE "competence" ADD CONSTRAINT "fk_competen_opop_6c62e0f5" FOREIGN KEY ("opop_id") REFERENCES "opop" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "competence" DROP CONSTRAINT "fk_competen_opop_6c62e0f5";
        DROP INDEX "idx_competence_code_6cf174";
        ALTER TABLE "competence" DROP COLUMN "code";
        ALTER TABLE "competence" DROP COLUMN "type";
        ALTER TABLE "competence" DROP COLUMN "opop_id";
        ALTER TABLE "competence" ALTER COLUMN "title" TYPE VARCHAR(128) USING "title"::VARCHAR(128);"""
