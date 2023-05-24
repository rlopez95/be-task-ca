from uuid import UUID

import pytest
from be_task_ca.user.domain.user import User, UserFactory, UserNotValidError


class TestUserFactory:
    def test_creates_user(self):
        user = UserFactory.make(
            email="some@mail.com",
            first_name="John",
            last_name="Doe",
            password="1234",
            shipping_address="nowhere",
            cart_items=[],
        )
        assert isinstance(user.id, UUID)
        assert isinstance(user, User)

    def test_raises_error_empty_name(self):
        with pytest.raises(UserNotValidError):
            UserFactory.make(
                email="some@mail.com",
                first_name="",
                last_name="Doe",
                password="1234",
                shipping_address="nowhere",
                cart_items=[],
            )

    def test_raises_error_empty_password(self):
        with pytest.raises(UserNotValidError):
            UserFactory.make(
                email="some@mail.com",
                first_name="John",
                last_name="Doe",
                password="",
                shipping_address="nowhere",
                cart_items=[],
            )
