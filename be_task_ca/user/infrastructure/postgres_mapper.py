from be_task_ca.user.domain.user import User
from be_task_ca.user.infrastructure.sql_alchemy_user import SqlAlchemyUser


def entity_to_postgres_model(user: User) -> SqlAlchemyUser:
    return SqlAlchemyUser(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=user.hashed_password,
        shipping_address=user.shipping_address,
        cart_items=user.cart_items,
    )


def postgres_model_to_entity(user: SqlAlchemyUser) -> User:
    return User(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=user.hashed_password,
        shipping_address=user.shipping_address,
        cart_items=user.cart_items,
    )
