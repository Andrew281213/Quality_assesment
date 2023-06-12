from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_kimapplicab_kim_id_2f55a5" ON "kimapplicability" ("kim_id", "discipline_competence_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "uid_kimapplicab_kim_id_2f55a5";"""
