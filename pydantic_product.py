from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше нуля")
    tags: list[str] = []
    market: Market


product_data = {
    "name": "milk",
    "price": 20.0,
    "tags": ["products"],
    "market": {
        "id": 1,
        "name": "Amazon"
    }
}

proguct = Product(**product_data)
print(proguct)