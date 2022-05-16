import uuid
from pydantic import BaseModel
from pydantic.typing import Optional, List

class FarmerBase(BaseModel): 
    id: Optional[int] = None
    username: str
    password: str
    email: str
    name: str
    phone: str

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "username": "Jhonin",
                "password": "jhon123",
                "email": "jhon@test.com",
                "name": "jhon kenedy",
                "phone": "999-999",
            }
        }


class FarmerUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    active_user: Optional[bool]
    automation_client: Optional[bool]

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "username": "Jhonin",
                "password": "jhon123",
                "email": "jhon@test.com",
                "name": "jhon kenedy",
                "phone": "999-999",
                "active_user": True,
                "automation_client": True
            }
        }


class FarmerList(BaseModel):
    username: str
    email: str
    name: str
    phone: str
    active_user: bool
    automation_client: bool

    class Config:
        orm_mode = True

class FarmerDetail(BaseModel):
    id: int
    username: str
    email: str
    name: str
    phone: str
    active_user: bool
    automation_client: bool

    class Config:
        orm_mode = True