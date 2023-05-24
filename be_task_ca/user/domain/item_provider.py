from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ItemSnap:
    item_id: UUID
    quantity: int


class ItemProvider(ABC):
    @abstractmethod
    def find_item_by_id(self, item_id: UUID) -> ItemSnap:
        raise NotImplementedError()


class ItemNotFoundError(Exception):
    ...
