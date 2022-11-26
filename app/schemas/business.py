from pydantic import BaseModel


class BusinessBase(BaseModel):
    name: str
    category: str
    location: str


class BusinessCreate(BusinessBase):
    location: str
    descriptionn: str

    class Config:
        orm_mode = True


class Business(BusinessBase):
    id_business: str
    description: str

    class Config:
        orm_mode = True


class BusinessPaginated(BaseModel):
    results: list[Business]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
