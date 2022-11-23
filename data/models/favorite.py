from sqlalchemy import Column, String, ForeignKey

from data import Base


class Favorite(Base):
    __tablename__ = 'favorite'
    id_favorite = Column(String(4), primary_key=True)
    id_business = Column(String(4), ForeignKey('business.id_business'))
    id_user = Column(String(4), ForeignKey('user.id_user'))
