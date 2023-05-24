from uuid import UUID
from fastapi.testclient import TestClient

from fastapi import status

from be_task_ca.app import app

print("FOOOO")
print(app)

client = TestClient(app)

def test_create_item():
    client.post(
        "/api/v1/items",
        json={
            "name": "Some name",
            "description": "Some description",
            "price": 5,
            "quantity": 10,
        },
    )
    
    response = client.get(
        "/api/v1/items",
    )

    assert response.status_code == status.HTTP_200_OK
    all_items = response.json()["items"]
    assert all_items is not []