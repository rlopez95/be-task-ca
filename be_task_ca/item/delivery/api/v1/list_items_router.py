from fastapi import APIRouter, Depends
from be_task_ca.item.infrastructure.in_memory_item_repository import (
    InMemoryItemRepository,
)

list_items_router = APIRouter()


async def _get_in_memory_item_repository() -> InMemoryItemRepository:
    return InMemoryItemRepository()


@list_items_router.get("/")
async def get_items(
    item_repository: InMemoryItemRepository = Depends(_get_in_memory_item_repository),
):
    return get_all(item_repository)
