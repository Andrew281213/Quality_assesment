from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "discipline" ADD "program_id" INT NOT NULL;
        ALTER TABLE "discipline" ADD "end_semester" INT NOT NULL;
        ALTER TABLE "discipline" ADD "code" VARCHAR(64) NOT NULL UNIQUE;
        CREATE UNIQUE INDEX "uid_discipline_code_e00b0f" ON "discipline" ("code");
        ALTER TABLE "discipline" ADD CONSTRAINT "fk_discipli_opop_5ce29e1c" FOREIGN KEY ("program_id") REFERENCES "opop" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "discipline" DROP CONSTRAINT "fk_discipli_opop_5ce29e1c";
        DROP INDEX "idx_discipline_code_e00b0f";
        ALTER TABLE "discipline" DROP COLUMN "program_id";
        ALTER TABLE "discipline" DROP COLUMN "end_semester";
        ALTER TABLE "discipline" DROP COLUMN "code";
        CREATE UNIQUE INDEX "uid_discipline_title_bf9c1b" ON "discipline" ("title");"""
