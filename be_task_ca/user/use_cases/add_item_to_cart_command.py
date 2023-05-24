from uuid import UUID
import uuid
from be_task_ca.shared.domain.command import Command
from be_task_ca.shared.domain.command_handler import CommandHandler
from be_task_ca.shared.domain.command_response import CommandResponse
from be_task_ca.user.domain.item_provider import (
    ItemNotFoundError,
    ItemProvider,
    ItemSnap,
)
from be_task_ca.user.domain.user import (
    CartItem,
    NotEnoughItemsInStockError,
    User,
    UserNotFound,
)
from be_task_ca.user.domain.user_repository import UserRepository


class AddItemToCartCommand(Command):
    def __init__(self, user_id: UUID, item_id: UUID, quantity: int) -> None:
        self.user_id = user_id
        self.item_id = item_id
        self.quantity = quantity
        super().__init__(uuid.uuid1())


class AddItemToCartCommandResponse(CommandResponse):
    def __init__(self, cart_items: list[CartItem]) -> None:
        self.cart_items = cart_items


class AddItemToCartCommandHandler(CommandHandler):
    def __init__(
        self, user_repository: UserRepository, item_provider: ItemProvider
    ) -> None:
        self._user_repository = user_repository
        self._item_provider = item_provider

    def process(self, command: AddItemToCartCommand) -> AddItemToCartCommandResponse:
        user: User | None = self._user_repository.find_user_by_id(command.user_id)
        if user is None:
            raise UserNotFound("User does not exist")

        item: ItemSnap | None = self._item_provider.find_item_by_id(command.item_id)
        if item is None:
            raise ItemNotFoundError()

        if item.quantity < command.quantity:
            raise NotEnoughItemsInStockError()

        new_cart_item: CartItem = CartItem(
            user_id=command.user_id, item_id=command.item_id, quantity=command.quantity
        )

        user.add_item_to_cart(new_cart_item)

        _ = self._user_repository.save_user(user)

        return AddItemToCartCommandResponse(user.cart_items)
