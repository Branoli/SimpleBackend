import asyncio

from aiohttp import web

from simple_backend.api.web_server import WebServer
from simple_backend.db.base import BaseDB


class SimpleBackendApp:
    def __init__(self, config):
        self.config = config
        self.host = self.config.api.host
        self.port = self.config.api.port

        self.db = BaseDB.factory(**config.provider)
        self.loop = asyncio.get_event_loop()
        self.web_sever = WebServer(self)

    def run(self):
        web.run_app(self.web_sever.web_server, host=self.host, port=self.port)
