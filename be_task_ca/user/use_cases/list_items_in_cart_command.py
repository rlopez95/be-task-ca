import uuid
from be_task_ca.shared.domain.command import Command
from be_task_ca.shared.domain.command_handler import CommandHandler
from be_task_ca.shared.domain.command_response import CommandResponse
from be_task_ca.user.domain.user import CartItem
from be_task_ca.user.domain.user_repository import UserRepository


class UserCartItemsCommand(Command):
    def __init__(self, user_id: uuid.UUID):
        self.user_id = user_id
        super().__init__(uuid.uuid1())


class UserCartItemsCommandResponse(CommandResponse):
    def __init__(self, cart_items: list[CartItem]):
        self.cart_items = cart_items


class UserCartItemsCommandHandler(CommandHandler):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def process(self, command: UserCartItemsCommand) -> UserCartItemsCommandResponse:
        cart_items = self._user_repository.find_cart_items_for_user_id(command.user_id)
        return UserCartItemsCommandResponse(cart_items)
