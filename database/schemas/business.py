from datetime import datetime
from sqlalchemy import Column, String, DateTime, BLOB, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Business (Base):
    __tablename__='business'
    id_business = Column(String(4), primary_key=True)
    id_user = Column(String(4), ForeignKey('user.id_user'))
    name_business = Column(String(50), nullable=False)
    location = Column(String(100), nullable= False)
    category = Column(String(70), nullable=False)
    image_logo=Column(BLOB, nullable=False)
    Date_of_Bith = Column(DateTime(), default=datetime.now())
    
    def __str__(self):
       return self.name_business