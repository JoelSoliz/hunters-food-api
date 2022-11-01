from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    surname: str
    password: str
    date_of_birth: datetime


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id_user: str
    name: str
    surname: str
    date_of_birth: datetime

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    access_token: str
    token_type: str
