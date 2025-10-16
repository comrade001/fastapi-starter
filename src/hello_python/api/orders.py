from fastapi import APIRouter, Path, Query
from pydantic import BaseModel
from .exceptions import InvalidOrderException

router = APIRouter(prefix="/orders", tags=["orders"])

class OrderOut(BaseModel):
    id: int
    total: float

@router.get("/{id}", response_model=OrderOut)
async def get_order(
    id: int = Path(..., ge=1), 
    vat: float = Query(0.0, ge=0, le=1),
    fail: bool = Query(False),
) -> OrderOut:
    if fail:
        raise InvalidOrderException(order_id=id, detail="forced failure for testing")
    base = id * 10.0
    return OrderOut(id=id, total = base * (1 + vat))