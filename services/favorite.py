from sqlalchemy.orm import Session

from data.models import Favorite
from schemas.favorite import FavoriteBase
from .utils import generate_id


class FavoriteService:
    def __init__(self, session: Session):
        self.session = session

    def add_favorite(self, id_user, id_business):
        id_favorite = generate_id()
        db_favorite = Favorite(id_favorite=id_favorite,
                               id_user=id_user, id_business=id_business)

        self.session.add(db_favorite)
        self.session.commit()
        self.session.refresh(db_favorite)

        return db_favorite
