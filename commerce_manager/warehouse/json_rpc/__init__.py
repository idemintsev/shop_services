import aiohttp_rpc
from aiohttp_rpc.errors import InvalidParams

from commerce_manager.warehouse.json_rpc import handlers


# Middlewares


async def internal_app_errors_handler(request, handler):
    try:
        error = None
        response = await handler(request)
    except Exception as exc:
        error = str(exc)

    if error:
        response = aiohttp_rpc.protocol.JsonRpcResponse(
            id=request.id,
            error=InvalidParams(data=error)
        )

    return response


# JSON RPC application


rpc_app = aiohttp_rpc.JsonRpcServer(
    middlewares=[
        aiohttp_rpc.middlewares.extra_args_middleware,
        internal_app_errors_handler,
    ],
)

rpc_app.add_methods([
    handlers.create_warehouse,
    handlers.edite_warehouse,
    handlers.get_list_warehouses,
    handlers.delete_warehouse,
    handlers.create_good,
    handlers.edit_good,
    handlers.get_list_goods,
    handlers.delete_good,
])
