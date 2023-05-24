
from uuid import UUID

import pytest
from be_task_ca.item.domain.item import ItemFactory, ItemNotValidError


class TestItemFactory:
    def test_creates_item(self):
        item = ItemFactory.make(name="Item", description="Description", price=10.50, quantity=100)
        assert isinstance(item.id, UUID)
    
    def test_raises_error_empty_name(self):
        with pytest.raises(ItemNotValidError):
            ItemFactory.make(name="", description="Description", price=10.50, quantity=100)

    def test_raises_error_empty_description(self):
        with pytest.raises(ItemNotValidError):
            ItemFactory.make(name="Name", description="", price=10.50, quantity=100)
        
    def test_raises_error_no_price(self):
        with pytest.raises(ItemNotValidError):
            ItemFactory.make(name="Name", description="Description", price=0, quantity=100)