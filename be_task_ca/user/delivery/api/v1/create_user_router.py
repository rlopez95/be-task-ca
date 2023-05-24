from fastapi import APIRouter, Depends, HTTPException, status

from be_task_ca.item.domain.item import ItemAlreadyExistsError
from be_task_ca.shared.domain.command_handler import CommandHandler
from be_task_ca.user.delivery.api.schemas.create_user_request import CreateUserRequest
from be_task_ca.user.delivery.api.schemas.create_user_response import CreateUserResponse
from be_task_ca.user.domain.user import UserAlreadyExistsError, UserNotValidError
from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepositoryFactory,
)
from be_task_ca.user.use_cases.create_user_command import (
    CreateUserCommandHandler,
    CreateUserCommand,
    CreateUserCommandResponse,
)


create_user_router = APIRouter()


async def _get_create_user_command_handler() -> CommandHandler:
    repository = InMemoryUserRepositoryFactory.make()
    return CreateUserCommandHandler(repository)


@create_user_router.post("/", response_model=CreateUserResponse)
async def post_customer(
    user_request: CreateUserRequest,
    handler: CreateUserCommandHandler = Depends(_get_create_user_command_handler),
):
    try:
        command = CreateUserCommand(
            user_request.email,
            user_request.first_name,
            user_request.last_name,
            user_request.password,
            user_request.shipping_address,
        )
        command_response: CreateUserCommandResponse = handler.process(command)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An user with this email adress already exists",
        )
    except UserNotValidError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is not valid",
        )

    return CreateUserResponse(
        id=command_response.user.id,
        first_name=command_response.user.first_name,
        last_name=command_response.user.last_name,
        email=command_response.user.email,
        shipping_address=command_response.user.shipping_address,
    )
