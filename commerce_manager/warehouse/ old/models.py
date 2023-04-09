import peewee as pw
from commerce_manager.settings import Config
import pendulum

db = pw.PostgresqlDatabase(
    Config.grpc.db.name,
    host=Config.grpc.db.host,
    port=Config.grpc.db.port,
    user=Config.grpc.db.user,
    password=Config.grpc.db.password
)


class BaseModel(pw.Model):

    class Meta:
        database = db


class Warehouse(BaseModel):
    id = pw.AutoField()
    name = pw.CharField(index=True, max_length=128)
    address = pw.TextField()
    latitude = pw.FloatField()
    longitude = pw.FloatField()
    created_at = pw.DateTimeField(default=pendulum.now())
    updated_at = pw.DateTimeField(default=pendulum.now())

    class Meta:
        db_table = 'warehouses'
