from concurrent.futures import ThreadPoolExecutor

import grpc

import warehouse_service.warehouse_manager_pb2_grpc as warehouse_manager
import warehouse_service.shop_manager_pb2_grpc as shop_manager
import warehouse_service.goods_manager_pb2_grpc as goods_manager

from warehouse_service.data import WarehouseData
from commerce_manager.settings import Config, logger

__version__ = "0.0.1"


class WareHouseManager(warehouse_manager.WarehouseManagerServiceServicer):
    def CreateWarehouse(self, request, context):
        warehouse = WarehouseData.from_request(request)
        breakpoint()

    def DeleteWarehouse(self, request, context):
        warehouse = WarehouseData.from_request(request)

    def ExistingWarehouses(self, request, context):
        pass


class GoodsManager(goods_manager.GoodsManagerServiceServicer):
    pass


class ShopManager(shop_manager.ShopManagerServiceServicer):
    pass


def serve() -> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    warehouse_service = WareHouseManager()
    shop_service = ShopManager()
    goods_service = GoodsManager()

    warehouse_manager.add_WarehouseManagerServiceServicer_to_server(warehouse_service, server)
    shop_manager.add_ShopManagerServiceServicer_to_server(shop_service, server)
    goods_manager.add_GoodsManagerServiceServicer_to_server(goods_service, server)
    server.add_insecure_port(Config.grpc.grpc_insecure_port)
    logger.info(f"Starting server on {Config.grpc.grpc_insecure_port}")

    server.start()
    server.wait_for_termination()
