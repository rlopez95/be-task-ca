from uuid import UUID
from sqlalchemy.orm import Session

from be_task_ca.item.domain.item import Item
from be_task_ca.item.domain.item_repository import ItemRepository


class PostgresItemRepository(ItemRepository):
    _repository = None

    def __init__(self, db: Session) -> None:
        self._db = db

    def save_item(self, item: Item) -> Item:
        self._db.add(item)
        self._db.commit()
        return item

    def get_all_items(self) -> list[Item]:
        return self._db.query(Item).all()

    def find_item_by_name(self, name: str) -> Item | None:
        return self._db.query(Item).filter(Item.name == name).first()

    def find_item_by_id(self, id: UUID) -> Item | None:
        return self._db.query(Item).filter(Item.id == id).first()
