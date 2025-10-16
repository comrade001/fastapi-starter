from httpx import AsyncClient, ASGITransport
from hello_python.api.main import app


async def test_ping():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/ping")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
