from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.user import User
from schemas.business import Business
from services.business import BusinessService
from services.favorite import FavoriteService

user_router = APIRouter(prefix='/user')


@user_router.get("/me", response_model=User, tags=["User"])
def get_me(user: User = Depends(get_current_user)):
    return user


@user_router.get('/business', response_model=Business, tags=["User"])
def get_business_by_user(session: Session = Depends(get_db_session), user: User = Depends(get_current_user)):
    business_service = BusinessService(session)
    get_business = business_service.get_user_business(user.id_user)
    if not get_business:
        raise HTTPException(
            status_code=404,
            detail=f"The user {user.id_user} does not have a registered business"
        )
    return get_business


@user_router.get('/favorite-business', tags=["User", "Favorite"])
def get_favorite_businesses_by_user(session: Session = Depends(get_db_session), user: User = Depends(get_current_user)):
    favorite_service = FavoriteService(session)
    favorite_businesses = favorite_service.get_favorites_by_user(user.id_user)

    return [business.id_business for business in favorite_businesses]
