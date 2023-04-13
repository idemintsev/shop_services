from attrs import asdict, frozen, filters, fields
from attrs_mate import AttrsClass

from commerce_manager.models import WarehouseModel


@frozen
class WarehouseBaseData(AttrsClass):
    id: int = AttrsClass.ib_int()
    name: str = AttrsClass.ib_str()
    address: str = AttrsClass.ib_str()
    latitude: float = AttrsClass.ib_float()
    longitude: float = AttrsClass.ib_float()
    created_at: str = AttrsClass.ib_str()
    updated_at: str = AttrsClass.ib_str()

    @classmethod
    def from_db(cls, data: WarehouseModel) -> 'WarehouseCreateDataResponse':
        return cls(
            id=data.id,
            name=data.name,
            address=data.address,
            latitude=data.latitude,
            longitude=data.longitude,
            created_at=data.created_at.strftime('%d.%m.%Y %H:%M:%S'),
            updated_at=data.updated_at.strftime('%d.%m.%Y %H:%M:%S')
        )


@frozen
class WarehouseCreateDataRequest(AttrsClass):
    name: str = AttrsClass.ib_str()
    address: str = AttrsClass.ib_str()
    latitude: float = AttrsClass.ib_float()
    longitude: float = AttrsClass.ib_float()


@frozen
class WarehouseCreateDataResponse(WarehouseBaseData):
    pass


@frozen
class WarehousesListData(AttrsClass):
    warehouses: list[WarehouseBaseData] = WarehouseBaseData.ib_list_of_nested()

    @classmethod
    def from_db(cls, data):
        return cls(
            warehouses=[WarehouseBaseData.from_db(warehouse) for warehouse in data]
        )


@frozen
class WarehouseEditeDataRequest(AttrsClass):
    id: int = AttrsClass.ib_int()
    name: str = AttrsClass.ib_str(default=None)
    address: str = AttrsClass.ib_str(default=None)
    latitude: float = AttrsClass.ib_float(default=None)
    longitude: float = AttrsClass.ib_float(default=None)

    def to_db(self):
        return asdict(self, filter=lambda k, v: v is not None and k.name != 'id')


@frozen
class WarehouseEditeDataResponse(WarehouseBaseData):
    pass


@frozen
class WarehouseDeleteData(AttrsClass):
    id: int = AttrsClass.ib_int()

    def to_response(self):
        return {'deleted': self.id}
