import uuid
from be_task_ca.shared.domain.command import Command
from be_task_ca.shared.domain.command_handler import CommandHandler
from be_task_ca.shared.domain.command_response import CommandResponse
from be_task_ca.user.domain.user import (
    User,
    UserAlreadyExistsError,
    UserFactory,
)
from be_task_ca.user.domain.user_repository import UserRepository


class CreateUserCommand(Command):
    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        password: str,
        shipping_address: str,
    ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.shipping_address = shipping_address
        super().__init__(uuid.uuid1())


class CreateUserCommandResponse(CommandResponse):
    def __init__(self, user: User) -> None:
        self.user = user


class CreateUserCommandHandler(CommandHandler):
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def process(self, command: CreateUserCommand) -> CreateUserCommandResponse:
        search_result = self._user_repository.find_user_by_email(command.email)
        if search_result is not None:
            raise UserAlreadyExistsError()

        new_user = UserFactory.make(
            command.email,
            command.first_name,
            command.last_name,
            command.password,
            command.shipping_address,
        )
        self._user_repository.save_user(new_user)
        return CreateUserCommandResponse(new_user)
