from uuid import UUID
from fastapi.testclient import TestClient

from fastapi import status

from be_task_ca.app import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/api/v1/users",
        json={
            "first_name": "John1",
            "last_name": "Doe",
            "email": "some1@example.com",
            "password": "abc1234",
            "shipping_address": "Somewhere",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    user_json = response.json()
    assert isinstance(UUID(user_json["id"]), UUID)
    assert user_json["first_name"] == "John1"
    assert user_json["last_name"] == "Doe"
    assert user_json["email"] ==  "some1@example.com"
    assert user_json.get("password") is None
    assert user_json["shipping_address"] == "Somewhere"
    
    
def test_create_same_user_raises_error():
    first_response = client.post(
        "/api/v1/users",
        json={
            "first_name": "Josh",
            "last_name": "Doe",
            "email": "exists@example.com",
            "password": "abc1234",
            "shipping_address": "Somewhere",
        },
    )
    assert first_response.status_code == status.HTTP_200_OK
    
    second_response = client.post(
        "/api/v1/users",
        json={
            "first_name": "Josh",
            "last_name": "Doe",
            "email": "exists@example.com",
            "password": "abc1234",
            "shipping_address": "Somewhere",
        },
    )
    
    assert second_response.status_code == status.HTTP_409_CONFLICT