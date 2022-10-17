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


class Product(ProductBase):
    id_product: str

    class Config:
        orm_mode = True
