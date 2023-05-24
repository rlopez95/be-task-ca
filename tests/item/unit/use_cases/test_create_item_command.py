
from unittest.mock import Mock

from be_task_ca.item.domain.item import ItemFactory
from be_task_ca.item.domain.item_repository import ItemRepository
from be_task_ca.item.use_cases.create_item_command import CreateItemCommand, CreateItemCommandHandler


def test_create_item():
    item = ItemFactory.make(name="Item", description="Description", price=10.50, quantity=100)
    command = CreateItemCommand(
        name=item.name, description=item.description, price=item.price, quantity=item.quantity
    )

    item_repository = Mock(ItemRepository)
    item_repository.find_item_by_name.return_value = None
    create_item_command_handler = CreateItemCommandHandler(item_repository)
    response = create_item_command_handler.process(command)

    item_repository.save_item.assert_called()
    assert response.item.name == item.name
    assert response.item.description == item.description
    assert response.item.price == item.price
    assert response.item.quantity == item.quantity