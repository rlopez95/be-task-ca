from pydantic import BaseModel

from be_task_ca.user.schema import AddToCartRequest


class AddToCartResponse(BaseModel):
    items: list[AddToCartRequest]
