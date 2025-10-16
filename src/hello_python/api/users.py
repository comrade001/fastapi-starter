from fastapi import APIRouter, Path
from pydantic import BaseModel, Field

router = APIRouter(prefix="/users", tags=["users"])

class UserIn(BaseModel):
    name: str = Field(min_length=1)

class UserOut(BaseModel):
    id: int
    name: str

@router.get("/{id}", response_model=UserOut)
async def get_user(id: int = Path(..., ge=1)) -> UserOut:
    return UserOut(id=id, name=f"user-{id}")