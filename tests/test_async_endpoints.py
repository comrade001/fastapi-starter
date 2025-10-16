import pytest
from httpx import AsyncClient, ASGITransport
from hello_python.api.main import app

@pytest.mark.asyncio
async def test_ping_async():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as ac:
        r = await ac.get("/ping")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_create_item_async():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {"name": "Latte", "price": 25.0}
        r = await ac.post("/items/5", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 5
    assert body["name"] == "Latte"
    assert body["price"] == 25.0


@pytest.mark.asyncio
async def test_orders_endpoint_async():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.get("/orders/2", params={"vat": 0.16})
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 2
    assert data["total"] == pytest.approx(23.2)