import uuid
from be_task_ca.item.domain.item import Item, ItemAlreadyExistsError, ItemFactory
from be_task_ca.item.domain.item_repository import ItemRepository
from be_task_ca.shared.domain.command import Command
from be_task_ca.shared.domain.command_handler import CommandHandler
from be_task_ca.shared.domain.command_response import CommandResponse


class CreateItemCommand(Command):
    def __init__(
        self, name: str, description: str | None, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__(uuid.uuid4())


class CreateItemCommandResponse(CommandResponse):
    def __init__(self, item: Item) -> None:
        self.item = item


class CreateItemCommandHandler(CommandHandler):
    def __init__(self, item_respository: ItemRepository) -> None:
        self._item_repository = item_respository

    def process(self, command: CreateItemCommand) -> CreateItemCommandResponse:
        search_result = self._item_repository.find_item_by_name(command.name)
        if search_result is not None:
            raise ItemAlreadyExistsError()

        new_item = ItemFactory.make(
            command.name,
            command.description,
            command.price,
            command.quantity,
        )
        self._item_repository.save_item(new_item)
        return CreateItemCommandResponse(new_item)
