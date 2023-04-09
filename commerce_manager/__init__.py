from aiohttp import web
from tortoise import Tortoise

from commerce_manager.warehouse.json_rpc import rpc_app
from commerce_manager.models import init_orm


async def db_ctx(app: 'web.Application'):
    """Connecting to database."""
    await init_orm()
    yield
    await Tortoise.close_connections()


async def asgi():
    app = web.Application()
    app.cleanup_ctx.append(db_ctx)

    app.add_routes([
        web.post('/rpc/v1', rpc_app.handle_http_request),
    ])

    return app
