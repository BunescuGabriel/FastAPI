from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None


class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True
