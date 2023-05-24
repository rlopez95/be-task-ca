from fastapi import APIRouter, Depends
from be_task_ca.item.delivery.api.schemas.all_items_response import AllItemsResponse
from be_task_ca.item.delivery.api.schemas.create_item_response import CreateItemResponse
from be_task_ca.item.infrastructure.in_memory_item_repository import (
    InMemoryItemRepository,
    InMemoryItemRepositoryFactory,
)
from be_task_ca.item.use_cases.list_all_items_user_command import (
    FindAllItemsCommand,
    FindAllItemsCommandHandler,
)

list_items_router = APIRouter()


async def _get_find_all_items_command_handler() -> FindAllItemsCommandHandler:
    item_repository = InMemoryItemRepositoryFactory.make()
    return FindAllItemsCommandHandler(item_repository)


@list_items_router.get("/", response_model=AllItemsResponse)
async def get_items(
    handler: FindAllItemsCommandHandler = Depends(_get_find_all_items_command_handler),
):
    command = FindAllItemsCommand()
    command_response = handler.process(command)
    return AllItemsResponse(
        items=[
            CreateItemResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                price=item.price,
                quantity=item.quantity,
            )
            for item in command_response.items
        ]
    )
