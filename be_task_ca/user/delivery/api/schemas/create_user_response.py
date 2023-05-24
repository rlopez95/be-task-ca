from uuid import UUID

from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    shipping_address: str | None
