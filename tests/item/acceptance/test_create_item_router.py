from uuid import UUID
from fastapi.testclient import TestClient

from fastapi import status

from be_task_ca.app import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/api/v1/items",
        json={
            "name": "Some name",
            "description": "Some description",
            "price": 5,
            "quantity": 10,
        },
    )

    assert response.status_code == status.HTTP_200_OK
    item_json = response.json()
    assert isinstance(UUID(item_json["id"]), UUID)
    assert item_json["name"] == "Some name"
    assert item_json["description"] == "Some description"
    assert item_json["price"] == 5
    assert item_json["quantity"] == 10