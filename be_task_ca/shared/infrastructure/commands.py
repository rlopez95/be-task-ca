from be_task_ca.shared.infrastructure.sqlalchemy_base import Base
from be_task_ca.shared.infrastructure.sqlalchemy_session import engine

# just importing all the models is enough to have them created
# flake8: noqa
from be_task_ca.user.infrastructure.sql_alchemy_user import (
    SqlAlchemyUser,
    SqlAlchemyCartItem,
)
from be_task_ca.item.infrastructure.sql_alchemy_item import SqlAlchemyItem


def create_db_schema():
    Base.metadata.create_all(bind=engine)
