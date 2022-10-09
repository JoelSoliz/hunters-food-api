from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


my_engine = create_engine('mysql://root:hunters_food-ramm@34.176.172.145:3306/hunters_food')
Base = declarative_base()

Session = sessionmaker(my_engine)
session = Session()

if __name__== '__main__':
    Base.metadata.drop_all(my_engine)
    Base.metadata.create_all(my_engine)
    