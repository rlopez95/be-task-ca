from fastapi import APIRouter

from be_task_ca.user.delivery.v1.api import (
    add_item_to_cart_router,
    create_user_router,
    list_item_in_cart_router,
)


user_router = APIRouter(
    prefix="/users/v1",
    tags=["users"],
)

user_router.include_router(create_user_router)
user_router.include_router(add_item_to_cart_router)
user_router.include_router(list_item_in_cart_router)
