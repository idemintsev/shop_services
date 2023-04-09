from attr import frozen, define, field
import os


@define(auto_attribs=True)
class WarehouseDBConfig:
    name: str = os.getenv('WAREHOUSE_SERVICE_DB_NAME', 'commerce_manager')
    host: str = os.getenv('WAREHOUSE_DB_HOST', 'localhost')
    port: int = int(os.getenv('WAREHOUSE_DB_PORT', 5432))
    user: str = os.getenv('WAREHOUSE_DB_USER', 'postgres')
    password: str = os.getenv('WAREHOUSE_DB_PASSWORD', 'postgres')

    @property
    def url(self):
        return f'asyncpg://{self.user}:{self.password}@localhost:5432/{self.name}'


@frozen
class WarehouseServiceConfig:
    host: str = os.getenv('WAREHOUSE_SERVICE_HOST', 'localhost')
    port: str = os.getenv('WAREHOUSE_SERVICE_PORT', '8080`')
    db: WarehouseDBConfig = WarehouseDBConfig()


@frozen
class ShopServicesConfig:
    mode: str = os.getenv('SHOP_SERVICES_MODE', 'DEBUG').lower()
    json_rpc: WarehouseServiceConfig = WarehouseServiceConfig()
    log_level: str = os.getenv('SHOP_SERVICES_LOG_LEVEL', 'ERROR').upper()


Config = ShopServicesConfig()

TORTOISE_ORM = {
    "connections": {"default": Config.json_rpc.db.url},
    "apps": {
        "models": {
            "models": ["commerce_manager.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
