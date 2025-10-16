import pytest
from httpx import AsyncClient, ASGITransport
from hello_python.api.main import app

@pytest.mark.asyncio
async def test_process_time_header_present():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as ac:
        r = await ac.get("/ping")
    assert r.status_code == 200
    h = r.headers.get("x-process-time")
    assert h is not None
    assert float(h) >= 0.0

@pytest.mark.asyncio
async def test_invalid_order_exception_handler():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as ac:
        r = await ac.get("/orders/7", params={"fail": "true"})
    assert r.status_code == 422
    body = r.json()
    assert body["error"] == "InvalidOrder"
    assert body["order_id"] == 7
    assert "forced failure" in body["detail"]
