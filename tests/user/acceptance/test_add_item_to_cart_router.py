from fastapi.testclient import TestClient

from fastapi import status

from be_task_ca.app import app

client = TestClient(app)

def test_add_item_to_cart():    
    create_item_response = client.post(
        "/api/v1/items",
        json={
            "name": "Some item",
            "description": "Some description",
            "price": 5,
            "quantity": 10,
        },
    )
    
    item_json = create_item_response.json()
    item_id = item_json["id"]
    
    create_user_response = client.post(
        "/api/v1/users",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "some@example.com",
            "password": "abc1234",
            "shipping_address": "Somewhere",
        },
    )
    
    user_json = create_user_response.json()
    user_id = user_json["id"]
    assert user_id is not None
    
    add_item_response = client.post(
        f"/api/v1/users/{user_id}/cart",
        json={
            "item_id": item_id,
            "quantity": 5,
        },
    )
    
    assert add_item_response.status_code == status.HTTP_200_OK
    