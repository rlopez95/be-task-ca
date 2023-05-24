from uuid import UUID
from pydantic import BaseModel


class AddToCartRequest(BaseModel):
    item_id: UUID
    quantity: int
