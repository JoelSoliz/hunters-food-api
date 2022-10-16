import math
from datetime import datetime
from sqlalchemy.orm import Session

from data.models import Product


class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def get_products(self, current_page, page_count=10):
        results = self.session.query(Product).offset(
            (current_page-1)*page_count).limit(page_count).all()  
        count_data = self.session.query(Product).filter(
            Product.final_time > datetime.now()).count()  

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
