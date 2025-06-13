from uuid import UUID
from fastapi import APIRouter, Depends
from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepository,
)
from be_task_ca.user.schema import AddToCartRequest

add_item_to_cart_router = APIRouter()


async def _get_in_memory_user_repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()


@add_item_to_cart_router.post("/{user_id}/cart")
async def post_cart(
    user_id: UUID,
    cart_item: AddToCartRequest,
    db: InMemoryUserRepository = Depends(_get_in_memory_user_repository),
):
    return add_item_to_cart(user_id, cart_item, db)
