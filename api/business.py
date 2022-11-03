from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.business import Business, BusinessCreate
from schemas.product import ProductPaginated
from schemas.user import User
from services.business import BusinessService
from services.product import ProductService

business_router = APIRouter(prefix='/business')


@business_router.get("/{id}", response_model=Business, tags=["Business"])
def get_businesss(id: str, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    business = business_service.get_business(id)
    if not business:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"posts id {id} not found. ")
    return business


@business_router.get("/{id}/products", response_model=ProductPaginated, tags=["Business", "Product"])
def get_products_by_business(id: str, current_page: int, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    return product_service.get_products(current_page, business=id)


@business_router.post('/register', response_model=Business, tags=["Business"])
def register_business(business: BusinessCreate = Depends(), image_logo: UploadFile = File(), session: Session = Depends(get_db_session), user: User = Depends(get_current_user)):
    business_service = BusinessService(session)
    return business_service.register_business(user.id_user, business, image_logo.file.read())
