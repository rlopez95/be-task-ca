from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from be_task_ca.item.infrastructure.in_memory_item_repository import (
    InMemoryItemRepositoryFactory,
)
from be_task_ca.user.delivery.api.schemas.add_to_cart_request import AddToCartRequest
from be_task_ca.user.delivery.api.schemas.add_to_cart_response import AddToCartResponse
from be_task_ca.user.domain.user import ItemAlreadyInCartError
from be_task_ca.user.infrastructure.in_memory_user_repository import (
    InMemoryUserRepositoryFactory,
)
from be_task_ca.user.infrastructure.item_provider_adapter import ItemProviderAdapter
from be_task_ca.user.use_cases.add_item_to_cart_command import (
    AddItemToCartCommand,
    AddItemToCartCommandHandler,
)


add_item_to_cart_router = APIRouter()


async def _get_add_item_command_handler() -> AddItemToCartCommandHandler:
    user_repository = InMemoryUserRepositoryFactory.make()
    item_repository = InMemoryItemRepositoryFactory.make()
    item_provider = ItemProviderAdapter(item_repository)
    return AddItemToCartCommandHandler(user_repository, item_provider)


@add_item_to_cart_router.post("/{user_id}/cart")
async def post_cart(
    user_id: UUID,
    cart_item: AddToCartRequest,
    handler: AddItemToCartCommandHandler = Depends(_get_add_item_command_handler),
):
    try:
        command = AddItemToCartCommand(user_id, cart_item.item_id, cart_item.quantity)
        command_response = handler.process(command)
        cart_items = [
            AddToCartRequest(item_id=item.item_id, quantity=item.quantity)
            for item in command_response.cart_items
        ]
        return AddToCartResponse(items=cart_items)
    except ItemAlreadyInCartError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Item already in cart"
        )
