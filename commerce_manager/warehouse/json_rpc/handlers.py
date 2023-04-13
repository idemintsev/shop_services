from commerce_manager.warehouse.json_rpc import data as dc
from commerce_manager.models import WarehouseModel, GoodModel


# Managing warehouses

async def create_warehouse(**params):
    req_data = dc.WarehouseCreateDataRequest.from_dict(params)
    warehouse = await WarehouseModel.create(**req_data.to_dict())
    res_data = dc.WarehouseCreateDataResponse.from_db(warehouse)
    return res_data.to_dict()


async def edite_warehouse(**params):
    req_data = dc.WarehouseEditeDataRequest.from_dict(params)
    if warehouse := await WarehouseModel.get_or_none(id=req_data.id):
        warehouse = warehouse.update_from_dict(req_data.to_db())
        await warehouse.save()
        res_data = dc.WarehouseEditeDataResponse.from_db(warehouse)
        return res_data.to_dict()
    return {'status': 'warehouse not found'}


async def get_list_warehouses(**params):
    warehouses = await WarehouseModel.all()
    res_data = dc.WarehousesListData.from_db(warehouses)
    return res_data.to_dict()


async def delete_warehouse(**params):
    req_data = dc.WarehouseDeleteData.from_dict(params)
    if warehouse := await WarehouseModel.get_or_none(id=req_data.id):
        await warehouse.delete()
        return req_data.to_response()


# Managing goods


async def create_good(**params):
    req_data = params
    res_data = params
    return res_data


async def edit_good(**params):
    req_data = params
    res_data = params
    return res_data


async def get_list_goods(**params):
    req_data = params
    res_data = params
    return res_data


async def delete_good(**params):
    req_data = params
    res_data = params
    return res_data
