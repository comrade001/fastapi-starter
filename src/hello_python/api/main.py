from fastapi import FastAPI
from .items import router as items_router
from .users import router as users_router
from .orders import router as orders_router
from .middleware import ProcessTimeMiddleware
from .exceptions import InvalidOrderException, invalid_order_handler


app = FastAPI()
app.add_middleware(ProcessTimeMiddleware)
app.add_exception_handler(InvalidOrderException, invalid_order_handler)

app.include_router(items_router)
app.include_router(users_router)
app.include_router(orders_router)


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"status": "ok"}
