from pydantic import BaseModel


class FavoriteBase(BaseModel):
    id_favorite: str


class Favorite(FavoriteBase):
    id_business: str
    id_user: str

    class Config:
        orm_mode = True
