from aerich import Command
from tortoise import Tortoise
from tortoise.models import Model
from tortoise import fields
from commerce_manager.settings import Config, TORTOISE_ORM
from datetime import datetime


async def init_orm() -> None:
    """Init Tortoise ORM in app."""
    await Tortoise.init(
        db_url=Config.json_rpc.db.url,
        modules={'models': ['commerce_manager.models']},
    )
    command = Command(tortoise_config=TORTOISE_ORM, app='models')
    await command.init()
    await command.upgrade()


class WarehouseModel(Model):
    id: fields.Field[int] = fields.IntField(pk=True)
    name: fields.Field[str] = fields.CharField(150, unique=True)
    address: fields.Field[str] = fields.TextField()
    latitude: fields.Field[float] = fields.FloatField(unique=True)
    longitude: fields.Field[float] = fields.FloatField(unique=True)
    goods: fields.ManyToManyRelation['GoodModel']

    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "warehouses"

    def __str__(self):
        return f'{self.id} {self.name}'

    def get_nearest_warehouse_with_good(self, latitude, longitude):
        row_sql = f'SELECT id, earth_distance(ll_to_earth(latitude, longitude), ' \
                  f'll_to_earth({latitude}, {longitude})) AS distance ' \
                  f'FROM {self.Meta.table} ' \
                  f'ORDER BY distance;'


class GoodModel(Model):
    id: fields.Field[int] = fields.IntField(pk=True)
    name: fields.Field[str] = fields.CharField(150, unique=True)
    code: fields.Field[str] = fields.CharField(128, unique=True)
    description: fields.Field[str] = fields.TextField()
    quantity: fields.Field[int] = fields.IntField()
    warehouse: fields.ManyToManyRelation['WarehouseModel'] = fields.ManyToManyField(
        'models.WarehouseModel', through='warehouses_goods', related_name='goods',
        backward_key='good_id', forward_key='warehouse_id')

    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "goods"

    def __str__(self):
        return f'{self.id} {self.code} {self.name}'
