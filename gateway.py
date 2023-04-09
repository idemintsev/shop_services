import os
import subprocess

import asyncclick as click
import uvloop

from commerce_manager import asgi  #noqa

uvloop.install()


async def warehouse_server():
    app_env = os.environ.copy()
    click.echo("Run warehouse server")
    subprocess.run("gunicorn gateway:asgi -c ./deploy/gunicorn.ini".split(' '), env=app_env)
