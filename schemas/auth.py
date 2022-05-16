from pydantic import BaseModel, ValidationError, root_validator
from typing import Optional

class SimpleUser(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    name: str

    class Config:
        orm_mode = True

class Password(BaseModel):

    password: str
    new_password: str
    confirm_password: str
    
    class Config:
        orm_mode = True

class ResetPassword(BaseModel):

    new_password: str
    confirm_password: str
    
    class Config:
        orm_mode = True

class ForgotPassword(BaseModel):
    email: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class LoginSuccess(BaseModel):
    user: SimpleUser
    access_token: str

    class Config:
        orm_mode = True