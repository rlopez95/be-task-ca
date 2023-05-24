from uuid import UUID

from be_task_ca.item.domain.item import Item
from be_task_ca.item.domain.item_repository import ItemRepository


class InMemoryItemRepository(ItemRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, Item] = {}

    def save_item(self, item: Item) -> Item:
        self._items[item.id] = item
        return item

    def get_all_items(self) -> list[Item]:
        return self._items.values()

    def find_item_by_name(self, name: str) -> Item | None:
        for item in self._items.values():
            if item.name == name:
                return item
        return None

    def find_item_by_id(self, id: UUID) -> Item | None:
        return self._items.get(id)


class InMemoryItemRepositoryFactory:
    _item_repository: InMemoryItemRepository = None

    @classmethod
    def make(cls) -> InMemoryItemRepository:
        if not isinstance(cls._item_repository, InMemoryItemRepository):
            cls._item_repository = InMemoryItemRepository()
        return cls._item_repository
