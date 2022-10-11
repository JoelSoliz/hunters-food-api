from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Discount (Base):
    __tablename__='discount'
    id_discount = Column(String(4), primary_key=True)
    id_product = Column(String(4), ForeignKey('product.id_product'))
    discount_ini = Column(DateTime(), nullable=False)
    discount_end = Column(DateTime(), nullable= False)
    