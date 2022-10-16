from pydantic import BaseModel


class BusinessBase(BaseModel):
    category: str


class BusinessCreate(BusinessBase):
    id_user: str
    name_business: str
    location: str
   


class Business(BusinessBase):
    name_business: str

    class Config:
        orm_mode = True