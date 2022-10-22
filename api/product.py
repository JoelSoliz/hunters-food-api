from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from .dependencies import get_current_user, get_db_session
from schemas.product import Product, ProductBase, ProductUpdate
from schemas.user import User
from services.product import ProductService


product_router = APIRouter(prefix='/product')


@product_router.get('/')
def get_products(current_page: int, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    return product_service.get_products(current_page)


@product_router.post('/register', response_model=Product)
def add_product(product: ProductBase = Depends(), image: UploadFile = File(), session: Session = Depends(get_db_session), _: User = Depends(get_current_user)):
    product_service = ProductService(session)
    return product_service.register_product(product, image.file.read())

@product_router.put('/update')
def update_product(id:str, product: ProductUpdate, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    return product_service.update_product(id, product)

