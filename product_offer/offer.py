from database.connect import session
from datetime import datetime
from database.schemas import Product
import math


def get_page_of_results(current_page, page_count=5):

    results = session.query(Product).offset((current_page-1)*page_count).limit(page_count).all()#restrict logging to return
    count_data = session.query(Product).filter(Product.final_time > datetime.now()).count()#count data from database

    if count_data:
        dictionary = {'results':list(results), 
                    'current_page':current_page,
                    'total_pages': math.trunc(count_data/page_count) ,
                    'total_elements':count_data, 
                    'element_per_page':page_count}
    else:
        dictionary = {'results': [], 
                    'current_page': 0,
                    'total_pages': 0,
                    'total_elements': 0, 
                    'element_per_page': 0}
                    
    return dictionary
