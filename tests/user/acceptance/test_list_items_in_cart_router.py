from fastapi.testclient import TestClient

from fastapi import status

from be_task_ca.app import app

client = TestClient(app)

def test_list_items_in_cart(): 
    new_user_response = client.post(
        "/api/v1/users",
        json={
            "first_name": "New",
            "last_name": "Doe",
            "email": "new-user@example.com",
            "password": "abc1234",
            "shipping_address": "Somewhere",
        },
    )
    
    user_json = new_user_response.json()
    user_id = user_json["id"]
    
    create_item_response = client.post(
        "/api/v1/items",
        json={
            "name": "New item",
            "description": "New description",
            "price": 5,
            "quantity": 10,
        },
    )
    
    item_json = create_item_response.json()
    item_id = item_json["id"]
    
    client.post(
        f"/api/v1/users/{user_id}/cart",
        json={
            "item_id": item_id,
            "quantity": 1,
        },
    )
    
    all_item_response = client.get(
        f"/api/v1/users/{user_id}/cart",
    )
    
    assert all_item_response.status_code == status.HTTP_200_OK
    
    items_in_cart = all_item_response.json()["items"]
    assert len(items_in_cart) == 1
    assert items_in_cart[0]["item_id"] == item_id
    
    
    