from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.business import Business, BusinessCreate
from schemas.user import User
from services.business import BusinessService

business_router = APIRouter(prefix='/business')


@business_router.post('/register', response_model=Business)
def register_business(business: BusinessCreate = Depends(), image_logo: UploadFile = File(), session: Session = Depends(get_db_session), user: User=Depends(get_current_user)):
    business_service = BusinessService(session)
    return business_service.register_business(user.id_user, business, image_logo.file.read())


@business_router.get("/{id}", response_model=Business)
def get_businesss(id: str, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    business = business_service.get_business(id)
    if not business:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts id {id} not found. ")  
    return business
