from fastapi import APIRouter
from be_task_ca.user.delivery.api.v1.add_item_to_cart_router import (
    add_item_to_cart_router,
)
from be_task_ca.user.delivery.api.v1.create_user_router import create_user_router
from be_task_ca.user.delivery.api.v1.list_items_in_cart_router import (
    list_items_in_cart_router,
)


user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
)

user_router.include_router(create_user_router)
user_router.include_router(add_item_to_cart_router)
user_router.include_router(list_items_in_cart_router)
