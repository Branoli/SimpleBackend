import json

from aiohttp import web


async def insert_new_visitors(request):
    db = request.app.api.db
    data = await request.post()
    if not data['name'] or not data['date']:
        web.Response(status=400)
    status = await db.visitors.insert_one(
        {'name': data['name'],
         'date': data['date']}
    )
    b = json.dumps({'status': status})
    try:
        return web.Response(status=201, body=b)
    except Exception as e:
        print(e)
