from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "kimapplicability" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "competence_id" INT NOT NULL REFERENCES "competence" ("id") ON DELETE CASCADE,
    "discipline_id" INT NOT NULL REFERENCES "discipline" ("id") ON DELETE CASCADE,
    "kim_id" INT NOT NULL REFERENCES "kim" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_kimapplicab_kim_id_976e4b" UNIQUE ("kim_id", "competence_id", "discipline_id")
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "kimapplicability";"""
