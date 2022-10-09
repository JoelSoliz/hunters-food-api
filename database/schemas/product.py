from datetime import datetime
from sqlalchemy import Column, String, DateTime, FLOAT, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product (Base):
    __tablename__='product'
    id_product = Column(String(4), primary_key=True)
    id_product_type = Column(String(4), ForeignKey('product_type'))
    id_business = Column(String(4), ForeignKey('business.id_business'))
    id_user = Column(String(4), ForeignKey('user.id_user'))
    name_product = Column(String(100), nullable=False)
    price = Column(FLOAT(10.2), nullable= False)
    image_product=Column(BLOB, nullable=False)
    Date_of_Bith = Column(DateTime(), default=datetime.now())
    
    def __str__(self):
       return self.name_product
