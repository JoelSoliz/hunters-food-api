from sqlalchemy.orm import Session

from data.models import FavoriteBusiness
from .utils import generate_id


class FavoriteService:
    def __init__(self, session: Session):
        self.session = session

    def add_favorite_business(self, id_user, id_business):
        id_favorite = generate_id()
        db_favorite = FavoriteBusiness(id_favorite=id_favorite,
                                       id_user=id_user, id_business=id_business)

        self.session.add(db_favorite)
        self.session.commit()
        self.session.refresh(db_favorite)

        return db_favorite

    def get_favorite(self, favorite_id, id_user) -> FavoriteBusiness:
        favorite = self.session.query(FavoriteBusiness).filter(
            FavoriteBusiness.id_favorite == favorite_id, FavoriteBusiness.id_user == id_user)
        return favorite.first()

    def get_favorites_by_user(self, id_user):
        favorites = self.session.query(FavoriteBusiness).filter(
            FavoriteBusiness.id_user == id_user)
        return favorites.all()

    def delete_favorite(self, id_favorite):
        self.session.query(FavoriteBusiness).filter(
            FavoriteBusiness.id_favorite == id_favorite).delete()
        self.session.commit()
