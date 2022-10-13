from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    surname: str
    password: str
    date_of_birth: datetime


class User(UserBase):
    name: str
    surname: str
    date_of_birth: datetime

    class Config:
        orm_mode = True
