from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base


class Discount(Base):
    __tablename__ = 'discount'
    id_discount = Column(String(4), primary_key=True)
    id_product = Column(String(4), ForeignKey('product.id_product'))
    discount_ini = Column(DateTime(), nullable=False)
    discount_end = Column(DateTime(), nullable=False)
