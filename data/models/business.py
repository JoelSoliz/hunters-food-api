from sqlalchemy import Column, String, LargeBinary, ForeignKey

from data import Base


class Business(Base):
    __tablename__ = 'business'
    id_business = Column(String(4), primary_key=True)
    id_user = Column(String(4), ForeignKey('user.id_user'))
    name = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    category = Column(String(70), nullable=False)
    logo = Column(LargeBinary((2**32)-1), nullable=False)
    description = Column(String(256), nullable=False)

    def __str__(self):
        return self.name
