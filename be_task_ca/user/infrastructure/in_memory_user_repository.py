from uuid import UUID
from be_task_ca.user.domain.user import User
from be_task_ca.user.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def save_user(self, user: User) -> User:
        self._users[user.id] = user
        return user

    def find_user_by_email(self, email: str) -> User | None:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def find_user_by_id(self, user_id: UUID) -> User | None:
        return self._users.get(user_id)

    def find_cart_items_for_user_id(self, user_id: UUID) -> list:
        user = self.find_user_by_id(user_id)
        if user is None:
            return []
        return user.cart_items


class InMemoryUserRepositoryFactory:
    _user_repository: InMemoryUserRepository = None

    @classmethod
    def make(cls) -> InMemoryUserRepository:
        if not isinstance(cls._user_repository, InMemoryUserRepository):
            cls._user_repository = InMemoryUserRepository()
        return cls._user_repository
