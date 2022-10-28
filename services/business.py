from sqlalchemy.orm import Session

from data.models.business import Business
from schemas.business import BusinessCreate
from .utils import generate_id


class BusinessService:
    def __init__(self, session: Session):
        self.session = session

    def register_business(self, id_user, business: BusinessCreate, logo):
        id_business = generate_id()
        db_business = Business(id_business=id_business, id_user=id_user, name=business.name, location=business.location,
                               category=business.category, logo=logo, description=business.descriptionn)

        self.session.add(db_business)
        self.session.commit()
        self.session.refresh(db_business)

        return db_business

    def get_business(self, business_id) -> Business:
        business = self.session.query(Business).filter(
            Business.id_business == business_id)
        return business.first()



