from fastapi import APIRouter, Path
from pydantic import BaseModel, Field, field_validator

router = APIRouter(prefix="/items", tags=["items"])

class ItemIn(BaseModel):
    name: str = Field(min_length=2)
    price: float | None = Field(default=None, ge=0)

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("name must not be empty")
        return v
    
    @field_validator("name", mode="before")
    @classmethod
    def strip_and_reject_blanks(cls, v: str) -> str:
        v = (v or "").strip()
        if not v:
            raise ValueError("name must not be empty")
        return v
    
class ItemOut(BaseModel):
    id: int
    name: str
    price: float | None = None

@router.post("/{id}", response_model=ItemOut)
async def upsert_item(
    id: int = Path(..., ge=1),
    payload: ItemIn | None = None,
) -> ItemOut:
    data = payload or ItemIn(name="unnamed")
    return ItemOut(id=id, name=data.name, price=data.price)    