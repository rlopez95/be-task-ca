from fastapi import APIRouter, Depends

from be_task_ca.user.delivery.v1.schemas.create_user_request import CreateUserRequest
from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepository,
)
from be_task_ca.user.use_cases.create_user_use_case import create_user


create_user_router = APIRouter()


async def _get_in_memory_user_repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()


@create_user_router.post("/")
async def post_customer(
    user: CreateUserRequest,
    user_repository: InMemoryUserRepository = Depends(_get_in_memory_user_repository),
):
    return create_user(user, user_repository=user_repository)
