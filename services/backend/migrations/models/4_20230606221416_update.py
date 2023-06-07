from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "studyplan" DROP CONSTRAINT "fk_studypla_group_7ac5d18f";
        ALTER TABLE "studyplan" RENAME COLUMN "group_id_id" TO "group_id";
        ALTER TABLE "studyplan" ADD "title" VARCHAR(128) NOT NULL UNIQUE;
        CREATE UNIQUE INDEX "uid_studyplan_title_48ea00" ON "studyplan" ("title");
        ALTER TABLE "studyplan" ADD CONSTRAINT "fk_studypla_group_1be6ff33" FOREIGN KEY ("group_id") REFERENCES "group" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "studyplan" DROP CONSTRAINT "fk_studypla_group_1be6ff33";
        DROP INDEX "idx_studyplan_title_48ea00";
        ALTER TABLE "studyplan" RENAME COLUMN "group_id" TO "group_id_id";
        ALTER TABLE "studyplan" DROP COLUMN "title";
        ALTER TABLE "studyplan" ADD CONSTRAINT "fk_studypla_group_7ac5d18f" FOREIGN KEY ("group_id_id") REFERENCES "group" ("id") ON DELETE CASCADE;"""
