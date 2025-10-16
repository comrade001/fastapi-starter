import pytest
from httpx import AsyncClient, ASGITransport
from hello_python.api.main import app

@pytest.mark.asyncio
async def test_item_ok():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.post("/items/10", json={"name": " Coffee ", "price": 12.5})
    assert res.status_code == 200
    assert res.json() == {"id": 10, "name": "Coffee", "price": 12.5}

@pytest.mark.asyncio
async def test_items_name_blanks_triggers_validator():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as ac:
        r = await ac.post("/items/1", json={"name": "   "})
    assert r.status_code == 422
    # opcional: confirma que es tu mensaje, no otro constraint
    # assert any(err["msg"] == "name must not be empty" for err in r.json()["detail"])