import hashlib
from fastapi import HTTPException
from be_task_ca.user.domain.user import User
from be_task_ca.user.domain.user_repository import UserRepository
from be_task_ca.user.schema import CreateUserRequest


def create_user(
    create_user: CreateUserRequest, user_repository: UserRepository
) -> User:
    search_result = user_repository.find_user_by_email(create_user.email)
    if search_result is not None:
        raise HTTPException(
            status_code=409, detail="An user with this email adress already exists"
        )

    new_user = User(
        first_name=create_user.first_name,
        last_name=create_user.last_name,
        email=create_user.email,
        hashed_password=hashlib.sha512(
            create_user.password.encode("UTF-8")
        ).hexdigest(),
        shipping_address=create_user.shipping_address,
    )

    return user_repository.save_user(new_user)
