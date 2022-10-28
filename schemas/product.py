from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    id_business: str
    name: str
    product_type: str
    price: float
    discount: float
    start_time: datetime
    final_time: datetime
    amount: int
    description: str


class Product(ProductBase):
    id_product: str

    class Config:
        orm_mode = True


class ProductPaginated(BaseModel):
    results: list[Product]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: str
    product_type: str
    price: float
    discount: float
    start_time: datetime
    final_time: datetime
    amount: int
    description: str
    class Config:
        orm_mode = True