from uuid import UUID
from sqlalchemy.orm import Session

from be_task_ca.item.domain.item import Item
from be_task_ca.item.domain.item_repository import ItemRepository
from be_task_ca.item.infrastructure.sql_alchemy_item import SqlAlchemyItem


class PostgresItemRepository(ItemRepository):
    _repository = None

    def __init__(self, db: Session) -> None:
        self._db = db

    def save_item(self, item: Item) -> Item:
        sql_item = self._entity_to_sql_user(item)
        self._db.add(sql_item)
        self._db.commit()
        return item

    def get_all_items(self) -> list[Item]:
        all_sql_items = self._db.query(SqlAlchemyItem).all()
        return (
            [self._sql_item_to_entity(sql_item) for sql_item in all_sql_items]
            if all_sql_items
            else []
        )

    def find_item_by_name(self, name: str) -> Item | None:
        sql_item = (
            self._db.query(SqlAlchemyItem).filter(SqlAlchemyItem.name == name).first()
        )
        return self._sql_item_to_entity(sql_item) if sql_item else None

    def find_item_by_id(self, id: UUID) -> Item | None:
        sql_item = (
            self._db.query(SqlAlchemyItem).filter(SqlAlchemyItem.id == id).first()
        )
        return self._sql_item_to_entity(sql_item) if sql_item else None

    def _entity_to_sql_user(self, item: Item) -> SqlAlchemyItem:
        return SqlAlchemyItem(
            item.id, item.name, item.description, item.price, item.quantity
        )

    def _sql_item_to_entity(self, sql_item: SqlAlchemyItem) -> Item:
        return Item(
            sql_item.id,
            sql_item.name,
            sql_item.description,
            sql_item.price,
            sql_item.quantity,
        )
