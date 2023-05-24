from uuid import UUID
from be_task_ca.item.domain.item_repository import ItemRepository
from be_task_ca.user.domain.item_provider import ItemProvider, ItemSnap


class ItemProviderAdapter(ItemProvider):
    def __init__(self, item_repository: ItemRepository) -> None:
        self._item_repository = item_repository

    def find_item_by_id(self, item_id: UUID) -> ItemSnap:
        item = self._item_repository.find_item_by_id(item_id)
        return ItemSnap(item.id, quantity=item.quantity)
