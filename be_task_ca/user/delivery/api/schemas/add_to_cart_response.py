from pydantic import BaseModel

from be_task_ca.user.delivery.api.schemas.add_to_cart_request import AddToCartRequest


class AddToCartResponse(BaseModel):
    items: list[AddToCartRequest]
