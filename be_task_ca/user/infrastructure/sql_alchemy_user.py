from dataclasses import dataclass
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from be_task_ca.shared.infrastructure.sqlalchemy_base import Base


@dataclass
class SqlAlchemyCartItem(Base):
    __tablename__ = "cart_items"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), primary_key=True, index=True
    )
    item_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("items.id"), primary_key=True)
    quantity: Mapped[int]


@dataclass
class SqlAlchemyUser(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4(),
        index=True,
    )
    email: Mapped[str] = mapped_column(unique=True, index=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    hashed_password: Mapped[str]
    shipping_address: Mapped[str] = mapped_column(default=None)
    cart_items: Mapped[list["SqlAlchemyCartItem"]] = relationship()
