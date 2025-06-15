from fastapi import APIRouter, Depends
from be_task_ca.item.delivery.api.schemas.create_item_request import CreateItemRequest
from be_task_ca.item.delivery.api.schemas.create_item_response import CreateItemResponse
from be_task_ca.item.infrastructure.in_memory_item_repository import (
    InMemoryItemRepository,
)


create_item_router = APIRouter()


async def _get_in_memory_item_repository() -> InMemoryItemRepository:
    return InMemoryItemRepository()


@create_item_router.post("/")
async def post_item(
    item: CreateItemRequest,
    item_repository: InMemoryItemRepository = Depends(_get_in_memory_item_repository),
) -> CreateItemResponse:
    return create_item(item, item_repository)
