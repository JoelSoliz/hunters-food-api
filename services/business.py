from sqlalchemy.orm import Session

from data.models.business import Business
from schemas.business import BusinessCreate
from .utils import generate_id


class BusinessService:
    def __init__(self, session: Session):
        self.session = session

    def register_business(self, business: BusinessCreate, logo):
        id_business = generate_id()
        db_business = Business(id_business=id_business, id_user=business.id_user, name_business=business.name_business, location=business.location,
                               category=business.category, image_logo=logo)

        self.session.add(db_business)
        self.session.commit()
        self.session.refresh(db_business)

        return db_business
