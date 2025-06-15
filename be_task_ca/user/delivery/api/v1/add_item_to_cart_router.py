from uuid import UUID
from fastapi import APIRouter, Depends
from be_task_ca.user.delivery.api.schemas.add_to_cart_request import AddToCartRequest
from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepository,
)
from be_task_ca.user.use_cases import add_item_to_cart_use_case


add_item_to_cart_router = APIRouter()


async def _get_in_memory_user_repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()


@add_item_to_cart_router.post("/{user_id}/cart")
async def post_cart(
    user_id: UUID,
    cart_item: AddToCartRequest,
    user_repository: InMemoryUserRepository = Depends(_get_in_memory_user_repository),
):
    return add_item_to_cart_use_case(user_id, cart_item, user_repository)
