from unittest.mock import Mock

from be_task_ca.item.domain.item import ItemFactory
from be_task_ca.item.domain.item_repository import ItemRepository
from be_task_ca.item.use_cases.create_item_command import CreateItemCommand, CreateItemCommandHandler
from be_task_ca.user.domain.user import UserFactory
from be_task_ca.user.domain.user_repository import UserRepository
from be_task_ca.user.use_cases.create_user_command import CreateUserCommand, CreateUserCommandHandler


def test_create_user_command():
    user = UserFactory.make(
        email="email@helu.com", first_name="foo", last_name="boo", password="abc", shipping_address="street"
    )
    command = CreateUserCommand(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.hashed_password,
        shipping_address=user.shipping_address,
    )

    user_repository = Mock(UserRepository)
    user_repository.find_user_by_email.return_value = None
    create_user_command_handler = CreateUserCommandHandler(user_repository)
    response = create_user_command_handler.process(command)

    user_repository.save_user.assert_called()
    assert response.user.email == user.email
    assert response.user.first_name == user.first_name
    assert response.user.last_name == user.last_name
    assert response.user.shipping_address == user.shipping_address
