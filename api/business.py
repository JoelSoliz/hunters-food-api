from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.business import Business, BusinessCreate, ShowBusiness
from schemas.user import User
from services.business import BusinessService

business_router = APIRouter(prefix='/business')


@business_router.post('/register', response_model=Business)
def register_business(business: BusinessCreate = Depends(), image_logo: UploadFile = File(), session: Session = Depends(get_db_session), user: User=Depends(get_current_user)):
    business_service = BusinessService(session)
    return business_service.register_business(user.id_user, business, image_logo.file.read())

@business_router.get("/{id}", response_model=ShowBusiness)
def get_businesss(id: str, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    return business_service.get_business(id)
