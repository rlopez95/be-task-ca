import hashlib
from pydantic.dataclasses import dataclass
import uuid


class ItemAlreadyInCartError(Exception):
    pass


class NotEnoughItemsInStockError(Exception):
    pass


@dataclass
class CartItem:
    user_id: uuid.UUID
    item_id: uuid.UUID
    quantity: int


class CartItemFactory:
    @staticmethod
    def make(user_id: uuid.UUID, item_id: uuid.UUID, quantity: int) -> CartItem:
        return CartItem(user_id, item_id, quantity)


@dataclass
class User:
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    hashed_password: str
    shipping_address: str
    cart_items: list[CartItem]

    def add_item_to_cart(self, cart_item: CartItem) -> None:
        item_ids = [o.item_id for o in self.cart_items]
        if cart_item.item_id in item_ids:
            raise ItemAlreadyInCartError()

        self.cart_items.append(cart_item)


class UserFactory:
    @staticmethod
    def make(
        email: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        password: str | None = None,
        shipping_address: str | None = None,
        cart_items: list[CartItem] | None = None,
    ) -> User:
        if email == "" or first_name == "" or password == "":
            raise UserNotValidError()

        return User(
            id=uuid.uuid4(),
            email=email,
            first_name=first_name,
            last_name=last_name,
            hashed_password=UserFactory._hash_password(password),
            shipping_address=shipping_address,
            cart_items=cart_items if cart_items else [],
        )

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()


class UserNotFound(Exception):
    pass


class UserNotValidError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass
