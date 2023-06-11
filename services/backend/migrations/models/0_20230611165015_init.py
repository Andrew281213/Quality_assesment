from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "direction" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "direction_code" VARCHAR(64) NOT NULL UNIQUE,
    "title" VARCHAR(128) NOT NULL
);
COMMENT ON COLUMN "direction"."direction_code" IS 'Шифр направления';
COMMENT ON COLUMN "direction"."title" IS 'Название направления';
CREATE TABLE IF NOT EXISTS "opop" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "program_code" VARCHAR(64) NOT NULL,
    "direction_code" VARCHAR(64) NOT NULL,
    "profile_title" VARCHAR(128) NOT NULL,
    "start_year" INT NOT NULL,
    CONSTRAINT "uid_opop_program_dcc281" UNIQUE ("program_code", "direction_code")
);
CREATE INDEX IF NOT EXISTS "idx_opop_program_c74c2a" ON "opop" ("program_code");
CREATE INDEX IF NOT EXISTS "idx_opop_directi_30960b" ON "opop" ("direction_code");
COMMENT ON COLUMN "opop"."program_code" IS 'Шифр программы';
COMMENT ON COLUMN "opop"."direction_code" IS 'Шифр направления';
COMMENT ON COLUMN "opop"."profile_title" IS 'Название профиля';
COMMENT ON COLUMN "opop"."start_year" IS 'Год начала программы';
CREATE TABLE IF NOT EXISTS "competence" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(128) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "kim" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text" TEXT NOT NULL,
    "img" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "discipline" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(128) NOT NULL UNIQUE
);
COMMENT ON COLUMN "discipline"."title" IS 'Наименование дисциплины';
CREATE TABLE IF NOT EXISTS "kimapplicability" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "competence_id" INT NOT NULL REFERENCES "competence" ("id") ON DELETE CASCADE,
    "discipline_id" INT NOT NULL REFERENCES "discipline" ("id") ON DELETE CASCADE,
    "kim_id" INT NOT NULL REFERENCES "kim" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_kimapplicab_kim_id_976e4b" UNIQUE ("kim_id", "competence_id", "discipline_id")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
