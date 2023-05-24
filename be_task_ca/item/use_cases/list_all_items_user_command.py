import uuid
from be_task_ca.item.domain.item import Item
from be_task_ca.item.domain.item_repository import ItemRepository
from be_task_ca.shared.domain.command import Command
from be_task_ca.shared.domain.command_handler import CommandHandler
from be_task_ca.shared.domain.command_response import CommandResponse


class FindAllItemsCommand(Command):
    def __init__(self) -> None:
        super().__init__(uuid.uuid1())


class FindAllItemsCommandResponse(CommandResponse):
    def __init__(self, items: list[Item]) -> None:
        self.items = items


class FindAllItemsCommandHandler(CommandHandler):
    def __init__(self, item_repository: ItemRepository) -> None:
        self._item_repository = item_repository

    def process(self, command: FindAllItemsCommand) -> FindAllItemsCommandResponse:
        items = self._item_repository.get_all_items()
        return FindAllItemsCommandResponse(items=items)
