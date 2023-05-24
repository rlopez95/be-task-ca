from uuid import UUID
from be_task_ca.user.domain.user import CartItem, User
from be_task_ca.user.domain.user_repository import UserRepository
from be_task_ca.user.infrastructure.sql_alchemy_user import (
    SqlAlchemyCartItem,
    SqlAlchemyUser,
)
from sqlalchemy.orm import Session


class PostgresUserRepository(UserRepository):
    _repository = None

    def __init__(self, db: Session) -> None:
        self._db = db

    def save_user(self, user: User) -> User:
        sql_user = self._entity_to_sql_user(user)
        self._db.add(sql_user)
        self._db.commit()
        return user

    def find_user_by_email(self, email: str) -> User | None:
        sql_user = (
            self._db.query(SqlAlchemyUser).filter(SqlAlchemyUser.email == email).first()
        )
        return self._sql_user_to_entity(sql_user) if sql_user else None

    def find_user_by_id(self, user_id: UUID) -> User | None:
        sql_user = (
            self._db.query(SqlAlchemyUser).filter(SqlAlchemyUser.id == user_id).first()
        )
        return self._sql_user_to_entity(sql_user) if sql_user else None

    def find_cart_items_for_user_id(self, user_id: UUID) -> list[CartItem]:
        sql_cart_items = (
            self._db.query(SqlAlchemyCartItem)
            .filter(SqlAlchemyCartItem.user_id == user_id)
            .all()
        )
        return (
            [self._sql_cart_item_to_entity(cart_item) for cart_item in sql_cart_items]
            if sql_cart_items
            else []
        )

    def _entity_to_sql_user(self, user: User) -> SqlAlchemyUser:
        return SqlAlchemyUser(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            hashed_password=user.hashed_password,
            shipping_address=user.shipping_address,
            cart_items=user.cart_items,
        )

    def _sql_user_to_entity(self, user: SqlAlchemyUser) -> User:
        return User(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            hashed_password=user.hashed_password,
            shipping_address=user.shipping_address,
            cart_items=user.cart_items,
        )

    def _sql_cart_item_to_entity(self, cart_item: SqlAlchemyCartItem) -> CartItem:
        return CartItem(cart_item.user_id, cart_item.item_id, cart_item.quantity)
