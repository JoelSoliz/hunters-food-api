import math
from datetime import datetime
from sqlalchemy.orm import Session

from data.models import Favorits
from schemas.favorits import FavoritsBase
from .utils import generate_id


class FavoritsService:
    def __init__(self, session: Session):
        self.session = session

    def add_favorits(self, favorits: FavoritsBase):
        id_favorits = generate_id()
        db_favorits = Favorits(id_favorits=id_favorits,
                               id_business=favorits.id_business)

        self.session.add(db_favorits)
        self.session.commit()
        self.session.refresh(db_favorits)

        return db_favorits
