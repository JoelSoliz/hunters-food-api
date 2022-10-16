from sqlalchemy.orm import Session

from data.models.user import User
from schemas.user import UserCreate, UserLogin
from .utils import create_access_token, generate_id, get_hashed_password, verify_password


class AuthenticationService:
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, user: UserCreate):
        hashed_password = get_hashed_password(user.password)
        id_user = generate_id()
        db_user = User(id_user=id_user, name=user.name, surname=user.surname, email=user.email.lower(),
                       hashed_password=hashed_password, date_of_birth=user.date_of_birth)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def get_user_by_email(self, email: str) -> User:
        user_filter = self.session.query(
            User).filter(User.email == email.lower())
        return user_filter.first()

    def authenticate_user(self, user: UserLogin):
        user_db = self.get_user_by_email(user.email)
        return not (not user_db or not verify_password(user.password, user_db.hashed_password))

    def login_session(self, user: UserLogin):
        return {
            "access_token": create_access_token(user.email),
            "token_type": "bearer"
        }
