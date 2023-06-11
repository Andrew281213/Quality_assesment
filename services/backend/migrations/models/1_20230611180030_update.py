from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "direction" RENAME COLUMN "code" TO "direction_code";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "direction" RENAME COLUMN "direction_code" TO "code";"""
