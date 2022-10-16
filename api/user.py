from fastapi import APIRouter, Depends

from api.dependencies import get_current_user
from schemas.user import User


user_router = APIRouter(prefix='/user')


@user_router.get("/me", response_model=User)
def get_me(user: User = Depends(get_current_user)):
    return user
