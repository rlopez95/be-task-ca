from abc import ABC, abstractmethod
from uuid import UUID

from be_task_ca.item.domain.item import Item


class ItemRepository(ABC):
    @abstractmethod
    def save_item(self, item: Item) -> Item:
        raise NotImplementedError()

    @abstractmethod
    def get_all_items(self) -> list[Item]:
        raise NotImplementedError()

    @abstractmethod
    def find_item_by_name(self, name: str) -> Item | None:
        raise NotImplementedError()

    @abstractmethod
    def find_item_by_id(self, id: UUID) -> Item | None:
        raise NotImplementedError()
