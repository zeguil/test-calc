import uuid
from pydantic import BaseModel
from pydantic.typing import Optional, List


class PartnerBase(BaseModel):
    id: Optional[int] = None
    username: str
    password: str
    email: str
    name: str
    phone: str
    brand: str
    logo_img: str
    website: str

    class Config:
        orm_mode = True

        schema_extra = {
                "example": {
                    "username": "Gabriel",
                    "password": "gabi123",
                    "email": "gb@email.com",
                    "name": "Gabriel Kenedy",
                    "phone": "999-999",
                    "brand": "autoponia",
                    "logo_img": "doc.png",
                    "website": "www.yoursite.com"

                }
        }


class PartnerUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    brand: Optional[str]
    logo_img: Optional[str]
    website: Optional[str]

    class Config:
        orm_mode = True


class PartnerList(BaseModel):
    username: str
    email: str
    name: str
    phone: str
    brand: str
    logo_img: str
    website: str

    class Config:
        orm_mode = True

class PartnerDetail(BaseModel):
    id: int
    username: str
    email: str
    name: str
    phone: str
    brand: str
    logo_img: str
    website: str

    class Config:
        orm_mode = True