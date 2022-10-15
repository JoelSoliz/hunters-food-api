from sqlalchemy.orm import Session

from data.models.user import User
from schemas.user import UserCreate
from .utils import generate_id, get_hashed_password


class AuthenticationService:
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, user: UserCreate):
        hashed_password = get_hashed_password(user.password)
        id_user = generate_id()
        db_user = User(id_user=id_user, name=user.name, surname=user.surname, email=user.email,
                       hashed_password=hashed_password, date_of_birth=user.date_of_birth)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def get_user_by_email(self, email: str):
        user_filter = self.session.query(User).filter(User.email == email)
        return user_filter.first()
