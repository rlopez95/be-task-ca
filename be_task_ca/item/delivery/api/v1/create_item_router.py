from fastapi import APIRouter, Depends, HTTPException, status
from be_task_ca.item.delivery.api.schemas.create_item_request import CreateItemRequest
from be_task_ca.item.delivery.api.schemas.create_item_response import CreateItemResponse
from be_task_ca.item.domain.item import ItemAlreadyExistsError, ItemNotValidError
from be_task_ca.item.infrastructure.in_memory_item_repository import (
    InMemoryItemRepositoryFactory,
)
from be_task_ca.item.use_cases.create_item_command import (
    CreateItemCommand,
    CreateItemCommandHandler,
)

create_item_router = APIRouter()


async def _get_create_item_command_handler() -> CreateItemCommandHandler:
    item_repository = InMemoryItemRepositoryFactory.make()
    return CreateItemCommandHandler(item_repository)


@create_item_router.post("/", response_model=CreateItemResponse)
async def post_item(
    item: CreateItemRequest,
    handler: CreateItemCommandHandler = Depends(_get_create_item_command_handler),
) -> CreateItemResponse:
    try:
        command = CreateItemCommand(
            item.name, item.description, item.price, item.quantity
        )
        command_response = handler.process(command)
    except ItemAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An item with this name already exists",
        )
    except ItemNotValidError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"""Item with name: {item.name},
            description: {item.description},
            price {item.price} and quantity {item.quantity} is not valid""",
        )

    return CreateItemResponse(
        name=command_response.item.name,
        description=command_response.item.description,
        price=command_response.item.price,
        quantity=command_response.item.quantity,
        id=command_response.item.id,
    )
