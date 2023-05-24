from pydantic import BaseModel

from be_task_ca.item.delivery.api.schemas.create_item_response import CreateItemResponse


class AllItemsResponse(BaseModel):
    items: list[CreateItemResponse]
