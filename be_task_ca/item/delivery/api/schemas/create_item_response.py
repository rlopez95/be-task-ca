from uuid import UUID

from be_task_ca.item.delivery.api.schemas.create_item_request import CreateItemRequest


class CreateItemResponse(CreateItemRequest):
    id: UUID
