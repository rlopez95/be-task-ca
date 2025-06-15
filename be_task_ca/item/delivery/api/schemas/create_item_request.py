from pydantic import BaseModel


class CreateItemRequest(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int
