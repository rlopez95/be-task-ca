from pydantic.dataclasses import dataclass
import uuid


@dataclass
class CartItem:
    user_id: uuid.UUID
    item_id: uuid.UUID
    quantity: int


@dataclass
class User:
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    hashed_password: str
    shipping_address: str
    cart_items: list[CartItem]
