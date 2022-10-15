from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.product import ProductService
from .dependencies import get_db_session


product_router = APIRouter(prefix='/product')


@product_router.get('/')
def get_products(current_page: int, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    return product_service.get_products(current_page)
