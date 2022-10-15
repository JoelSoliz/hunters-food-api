from sqlalchemy import Column, String, DateTime

from data import Base


class User(Base):
    __tablename__ = 'user'
    id_user = Column(String(4), primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    email = Column(String(70), nullable=False)
    hashed_password = Column(String(60), nullable=False)
    date_of_birth = Column(DateTime())

    def __str__(self) -> str:
        return f'user(id={self.id_user}, name={self.name}, surname={self.email}, date_of_birth={self.date_of_birth})'
