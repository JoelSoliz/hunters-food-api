from pydantic import BaseModel


class BusinessBase(BaseModel):
    name: str
    category: str


class BusinessCreate(BusinessBase):
    location: str
    descriptionn: str
    class Config:
        orm_mode = True
   

class Business(BusinessBase):
    id_business: str

    class Config:
        orm_mode = True

class ShowBusiness(BusinessBase):
    id_business: str
    location: str
    description: str
    class Config:
        orm_mode = True