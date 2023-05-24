from fastapi import APIRouter

from be_task_ca.item.delivery.api.v1.create_item_router import create_item_router
from be_task_ca.item.delivery.api.v1.list_items_router import list_items_router


item_router = APIRouter(
    prefix="/api/v1/items",
    tags=["items"],
)

item_router.include_router(create_item_router)
item_router.include_router(list_items_router)
