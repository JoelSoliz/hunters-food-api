from sqlalchemy import Column, String, DateTime, FLOAT, ForeignKey, LargeBinary, Integer

from data import Base


class Favorits(Base):
    __tablename__ = 'favorits'
    id_favorit = Column(String(4), primary_key=True)
    id_business = Column(String(4), ForeignKey('business.id_business'))
