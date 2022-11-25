from sqlalchemy import Column, String

from data import Base


class Product_type(Base):
    __tablename__ = 'product_type'
    id_product_type = Column(String(4), primary_key=True)
    type = Column(String(8), nullable=False)
