from aiohttp import web

from simple_backend.api.views.get_visitors import get_visitors
from simple_backend.api.views.insert_new_visitors import insert_new_visitors


class WebServer:
    def __init__(self, app):
        self.web_server = web.Application()
        self.web_server.api = app
        routes = [
            web.route('GET', '/visitors', get_visitors),
            web.route('POST', '/visitors', insert_new_visitors),
        ]
        self.web_server.add_routes(routes)
