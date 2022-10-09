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
    Date_of_Bith = Column(DateTime(), default=datetime.now())

    def __str__(self) -> str:
        #f'user(id={self.id_user})'
       return 'User(id= %s, name= %s, suername=%s, email= %s,password=%s, Date_of_Bith=%s)' %(self.id_user, self.name, self.surname, self.email, self.password, self.Date_of_Bith)

#if __name__== '__main__':
 #   Database.Base.metadata.drop_all(Database.my_engine)
  #  Database.Base.metadata.create_all(Damy_engine)
