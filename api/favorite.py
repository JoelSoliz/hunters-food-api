from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session


from .dependencies import get_current_user, get_db_session
from schemas.favorite import Favorite, FavoriteBase
from schemas.user import User
from services.favorite import FavoriteService


favorite_router = APIRouter(prefix='/favorite')


@favorite_router.post('/add', response_model=Favorite, tags=["Favorite"])
def add_favorite(id_business,
                 session: Session = Depends(get_db_session),
                 user: User = Depends(get_current_user)
                 ):
    favorite_service = FavoriteService(session)
    favorite_business = favorite_service.add_favorite(
        user.id_user, id_business)
    return favorite_business
