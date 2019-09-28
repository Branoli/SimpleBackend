import logging

from simple_backend.db.mongo.mongo import Mongo


class Visitors(Mongo):
    collection_name = 'visitors'

    @classmethod
    async def get(cls, limit=5000, **kwargs):
        return await cls.collection.find(kwargs).to_list(length=limit)

    @classmethod
    async def get_one(self):
        pass

    @classmethod
    async def insert_one(cls, item, *args, **kwargs):
        if not await cls.collection.find_one(item):
            result = await cls.collection.insert_one(item)
            logging.info(f'Inserted visitor with {result.inserted_id}')
            return True
        else:
            logging.info(f"There is already visitors with user {item['name']}")
            return False

    @classmethod
    async def delete_one(cls):
        pass

    @classmethod
    async def delete_many(cls):
        pass
