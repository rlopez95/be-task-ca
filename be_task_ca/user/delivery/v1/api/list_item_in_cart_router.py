from uuid import UUID
from fastapi import APIRouter, Depends

from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepository,
)


list_items_in_cart_router = APIRouter()


async def _get_in_memory_user_repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()


@list_items_in_cart_router.get("/{user_id}/cart")
async def get_cart(
    user_id: UUID, db: InMemoryUserRepository = Depends(_get_in_memory_user_repository)
):
    return list_items_in_cart(user_id, db)
