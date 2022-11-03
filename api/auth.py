from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db_session
from schemas.user import User, UserCreate, UserLogin, UserToken
from services.auth import AuthenticationService


auth_router = APIRouter(prefix='/auth')


@auth_router.post('/signup', response_model=User, tags=["User"])
def register_user(user: UserCreate, session: Session = Depends(get_db_session)):
    auth_service = AuthenticationService(session)
    db_user = auth_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return auth_service.register_user(user)


@auth_router.post('/login', response_model=UserToken, tags=["User"])
def login(user: UserLogin, session: Session = Depends(get_db_session)):
    auth_service = AuthenticationService(session)
    if not auth_service.authenticate_user(user):
        raise HTTPException(
            status_code=400, detail="Incorrect email or password.")

    return auth_service.login_session(user)
