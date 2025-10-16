import pytest
from httpx import AsyncClient, ASGITransport
from hello_python.api.main import app

@pytest.mark.asyncio
async def test_users():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as ac:
        r = await ac.get("/users/2")
    assert r.status_code == 200
    assert r.json() == {"id": 2, "name": "user-2"}

@pytest.mark.asyncio
async def test_orders_with_vat():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as ac:
        r = await ac.get("/orders/3", params={"vat": 0.16})
    assert r.status_code == 200
    assert r.json()["id"] == 3
    assert r.json()["total"] == pytest.approx(34.8)
