from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User (Base):
    __tablename__='user'
    id_user = Column(String(4), primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable= False)
    email = Column(String(70), nullable=False)
    password=Column(String(15), nullable=False)
    date_of_birth = Column(DateTime(), default=datetime.now())

    def __str__(self) -> str:
        return f'user(id={self.id_user}, name={self.name}, surname={self.email}, password={self.password}, date_of_bith={self.date_of_birth})'
       