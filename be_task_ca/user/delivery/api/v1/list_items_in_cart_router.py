from uuid import UUID
from fastapi import APIRouter, Depends

from be_task_ca.user.delivery.api.schemas.add_to_cart_request import AddToCartRequest
from be_task_ca.user.delivery.api.schemas.add_to_cart_response import AddToCartResponse
from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepositoryFactory,
)
from be_task_ca.user.use_cases.list_items_in_cart_command import (
    UserCartItemsCommand,
    UserCartItemsCommandHandler,
    UserCartItemsCommandResponse,
)

list_items_in_cart_router = APIRouter()


async def _get_user_items_list_command_handler() -> UserCartItemsCommandHandler:
    user_repository = InMemoryUserRepositoryFactory.make()
    return UserCartItemsCommandHandler(user_repository)


@list_items_in_cart_router.get("/{user_id}/cart")
async def get_cart(
    user_id: UUID,
    handler: UserCartItemsCommandHandler = Depends(
        _get_user_items_list_command_handler
    ),
) -> AddToCartResponse:
    command = UserCartItemsCommand(user_id)
    command_response: UserCartItemsCommandResponse = handler.process(command)
    cart_items = [
        AddToCartRequest(item_id=item.item_id, quantity=item.quantity)
        for item in command_response.cart_items
    ]
    return AddToCartResponse(items=cart_items)
