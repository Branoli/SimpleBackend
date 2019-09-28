import os

import yaml
import pymongo
from invoke import task
from pathlib import Path


@task
def start_api(ctx):
    from simple_backend.app import SimpleBackendApp
    simple_backend_app = SimpleBackendApp(ctx.config)


@task
def mongo_loadfixtures(ctx):
    mongo_uri = os.getenv('MONGO') or 'mongodb://localhost:27017/'
    mongo = pymongo.MongoClient(mongo_uri)
    db = mongo['simple_db']

    dir = Path(__file__).parent / 'simple_backend' / 'db' / 'mongo' / 'fixtures'
    for fixture in dir.glob('*.yaml'):
        collection = fixture.stem
        db.drop_collection(collection)
        data = yaml.load(fixture.read_text(encoding='utf-8'), Loader=yaml.FullLoader)
        db[collection].insert(data)
