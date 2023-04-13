from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "goods" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(150) NOT NULL UNIQUE,
    "code" VARCHAR(128) NOT NULL UNIQUE,
    "description" TEXT NOT NULL,
    "quantity" INT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "warehouses" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(150) NOT NULL UNIQUE,
    "address" TEXT NOT NULL,
    "latitude" DOUBLE PRECISION NOT NULL UNIQUE,
    "longitude" DOUBLE PRECISION NOT NULL UNIQUE,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "warehouses_goods" (
    "good_id" INT NOT NULL REFERENCES "goods" ("id") ON DELETE CASCADE,
    "warehouse_id" INT NOT NULL REFERENCES "warehouses" ("id") ON DELETE CASCADE
);
CREATE EXTENSION IF NOT EXISTS cube;
CREATE EXTENSION IF NOT EXISTS earthdistance;
"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
