from pydantic import BaseModel
from pydantic.typing import Optional

class AdminBase(BaseModel):
    id: Optional[int] = None
    username: str
    password: str
    email: str
    name: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True

class AdminList(BaseModel):
    username: str
    email: str
    name: Optional[str]

    class Config:
        orm_mode = True
