import pytest


@pytest.mark.parametrize(
    ('name', 'date'),
    (
            ('Гвидо ван Россум', 'datetime::2019-01-01T00:00:00.000'),
    )
)
async def test_simple_backend_app(aiohttp_client, create_app,
                                  name, date):
    data = {}
    if name:
        data['name'] = name
    if date:
        data['date'] = date

    client = await aiohttp_client(create_app)
    r = await client.post('/visitors', data=data)
    assert 201 == r.status, await r.text()
    pass
