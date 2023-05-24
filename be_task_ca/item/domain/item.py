from dataclasses import dataclass
from uuid import UUID
import uuid


@dataclass
class Item:
    id: UUID
    name: str
    description: str
    price: float
    quantity: int


class ItemFactory:
    @staticmethod
    def make(name: str, description: str, price: float, quantity: int) -> Item:
        if name == "" or description == "":
            raise ItemNotValidError()

        if not price:
            raise ItemNotValidError()

        return Item(uuid.uuid4(), name, description, price, quantity)


class ItemNotValidError(Exception):
    pass


class ItemNotFound(Exception):
    pass


class ItemAlreadyExistsError(Exception):
    pass
