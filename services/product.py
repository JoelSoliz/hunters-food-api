import math
from datetime import datetime
from sqlalchemy.orm import Session

from data.models import Product
from schemas.product import ProductBase
from .utils import generate_id


class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def get_products(self, current_page, page_count=10):
        results = self.session.query(Product).filter(Product.final_time > datetime.now()).order_by(Product.final_time).offset(
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

    def register_product(self, product: ProductBase, image):
        id_product = generate_id()
        db_product = Product(id_product=id_product, id_business=product.id_business,
                             name=product.name, price=product.price, product_type=product.product_type, image=image, discount=product.discount, amount=product.amount, start_time=product.start_time, final_time=product.final_time, description=product.description)

        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)

        return db_product

    def get_product(self, product_id) -> Product:
        product = self.session.query(Product).filter(
            Product.id_product == product_id)
        return product.first()

    def update_product(self, id, image, product: ProductBase, get_product):
        self.session.query(Product).filter(Product.id_product == id).update({'id_business':product.id_business,
                                                                             'name': product.name,
                                                                             'product_type': product.product_type,
                                                                             'image': image, 'price': product.price,
                                                                             'discount': product.discount,
                                                                             'start_time': product.start_time,
                                                                             'final_time': product.final_time,
                                                                             'amount': product.amount,
                                                                             'description': product.description})
        self.session.commit()
        self.session.refresh(get_product)
        return get_product
