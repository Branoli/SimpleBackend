import os

from motor import motor_asyncio

from simple_backend.common.utils import classproperty, convert_class_name
from simple_backend.db.base import BaseDB


class Mongo(BaseDB):
    collection_name = NotImplemented
    models = {}
    db = None

    def __init__(self, host, port, db_name, **kwargs):
        self.url = os.getenv('MONGO', f"mongodb://{host}:{port}/")
        self.mongo = motor_asyncio.AsyncIOMotorClient(self.url)
        Mongo.db = self.mongo[db_name]
        pass

    def __init_subclass__(cls, **kwargs):
        cls.models[convert_class_name(cls.__name__)] = cls

    def __getattr__(self, item):
        return self.models[item]

    def __getitem__(self, item):
        return self.db[self.collection_name]

    @classproperty
    def collection(self):
        return self.db[self.collection_name]
