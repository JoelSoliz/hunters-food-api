from pydantic import BaseModel


class FavoriteBusinessBase(BaseModel):
    id_favorite: str


class FavoriteBusiness(FavoriteBusinessBase):
    id_business: str
    id_user: str

    class Config:
        orm_mode = True
