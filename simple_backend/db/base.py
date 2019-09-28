from simple_backend.common.utils import convert_class_name


class BaseDB:
    providers = {}

    def __init_subclass__(cls, **kwargs):
        cls.providers[convert_class_name(cls.__name__)] = cls

    @classmethod
    def factory(cls, name, config):
        return cls.providers[name](**config)

    @classmethod
    async def get(self):
        pass

    @classmethod
    async def get_one(self):
        pass

    @classmethod
    async def insert_one(self, item, *args, **kwargs):
        pass

    @classmethod
    async def delete_one(self):
        pass

    @classmethod
    async def delete_many(self):
        pass
