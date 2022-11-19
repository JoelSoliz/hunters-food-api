from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.user import User
from schemas.business import Business
from services.business import BusinessService
user_router = APIRouter(prefix='/user')


@user_router.get("/me", response_model=User, tags=["User"])
def get_me(user: User = Depends(get_current_user)):
    return user

@user_router.get('/business', response_model=Business, tags=["User"])
def get_business_by_user(session: Session = Depends(get_db_session), user: User = Depends(get_current_user)):
    business_service = BusinessService(session)
    return business_service.get_user_business(user.id_user)
