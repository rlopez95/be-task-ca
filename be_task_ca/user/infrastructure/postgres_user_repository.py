from uuid import UUID
from be_task_ca.user.domain.user_repository import UserRepository
from be_task_ca.user.infrastructure.sql_alchemy_user import SqlAlchemyUser
from sqlalchemy.orm import Session


class PostgresUserRepository(UserRepository):
    _repository = None

    def __init__(self, db: Session) -> None:
        self._db = db

    def save_user(self, user: User):
        self._db.add(user)
        self._db.commit()
        return user

    def find_user_by_email(self, email: str) -> User:
        return self._db.query(User).filter(User.email == email).first()

    def find_user_by_id(self, user_id: UUID) -> User:
        return self._db.query(User).filter(User.id == user_id).first()

    def find_cart_items_for_user_id(self, user_id) -> list[User]:
        return (
            self._db.query(SqlAlchemyUser)
            .filter(SqlAlchemyUser.user_id == user_id)
            .all()
        )
