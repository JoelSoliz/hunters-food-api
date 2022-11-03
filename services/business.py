import math
from datetime import datetime
from sqlalchemy.orm import Session

from data.models.business import Business
from schemas.business import BusinessCreate
from .utils import generate_id


class BusinessService:
    def __init__(self, session: Session):
        self.session = session

    def get_Business(self, current_page, page_count=10):
        results = self.session.query(Business).offset(
            (current_page-1)*page_count).limit(page_count).all()
        count_data = self.session.query(Business).filter(
            Business.final_time > datetime.now()).count()

        if count_data:
            dictionary = {'results': list(results),
                          'current_page': current_page,
                          'total_pages': math.ceil(count_data / page_count),
                          'total_elements': count_data,
                          'element_per_page': page_count}
        else:
            dictionary = {'results': [],
                          'current_page': 0,
                          'total_pages': 0,
                          'total_elements': 0,
                          'element_per_page': 0}

        return dictionary

    def register_business(self, id_user, business: BusinessCreate, logo):
        id_business = generate_id()
        db_business = Business(id_business=id_business, id_user=id_user, name=business.name, location=business.location,
                               category=business.category, logo=logo, description=business.descriptionn)

        self.session.add(db_business)
        self.session.commit()
        self.session.refresh(db_business)

        return db_business

    def check_business_by_user(self, id_user, id_business):
        business = self.session.query(Business).filter(
            Business.id_business == id_business).first()

        if not business:
            return False

        return business.id_user == id_user
        
    def get_business(self, business_id) -> Business:
        business = self.session.query(Business).filter(
            Business.id_business == business_id)
        return business.first()
