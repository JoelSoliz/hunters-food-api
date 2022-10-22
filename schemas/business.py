from pydantic import BaseModel


class BusinessBase(BaseModel):
    name: str
    category: str


class BusinessCreate(BusinessBase):
    location: str
    descriptionn: str


class Business(BusinessBase):
    id_business: str

    class Config:
        orm_mode = True