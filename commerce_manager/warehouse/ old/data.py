from attr import define, field, asdict

from warehouse_service.warehouse_manager_pb2 import CreateRequest


@define
class WarehouseData:
    name: str
    address: str
    location: 'GeoPointData'
    created_at: int = 0
    updated_at: int = 0

    @classmethod
    def from_request(cls, data: CreateRequest) -> 'WarehouseData':
        return cls(
            name=data.name,
            address=data.address,
            location=GeoPointData.from_request(data),
        )

    def to_db(self) -> dict:
        return asdict(self)


@define
class GeoPointData:
    lon: float = field(converter=float)
    lat: float = field(converter=float)

    @classmethod
    def from_request(cls, data: CreateRequest) -> 'GeoPointData':
        return cls(lon=data.location.lon, lat=data.location.lat)
