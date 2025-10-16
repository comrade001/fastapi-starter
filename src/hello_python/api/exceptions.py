from fastapi import Request
from fastapi.responses import JSONResponse

class InvalidOrderException(Exception):
    def __init__(self, order_id: int, detail: str = "invalid order"):
        self.order_id = order_id
        self.detail = detail

async def invalid_order_handler(_request: Request, exc: InvalidOrderException):
    return JSONResponse(
        status_code=422,
        content={"error": "InvalidOrder", "order_id": exc.order_id, "detail": exc.detail},
    )