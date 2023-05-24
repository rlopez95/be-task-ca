from abc import ABC, abstractmethod
from uuid import UUID

from be_task_ca.user.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def save_user(self, User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def find_user_by_email(self, email: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    def find_user_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    def find_cart_items_for_user_id(self, user_id) -> list[User]:
        raise NotImplementedError()
