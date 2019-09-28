import pathlib

import pytest
from invoke import Config

from simple_backend.app import SimpleBackendApp


@pytest.fixture
def base_config():
    path = str(pathlib.Path(__file__).parent.parent) + '/'
    config = Config(system_prefix=path)
    return config


@pytest.fixture
def create_app(loop, base_config):
    web_server_app = SimpleBackendApp(base_config)
    return web_server_app.web_sever.web_server
