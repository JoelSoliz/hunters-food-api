from datetime import datetime
from pydantic import BaseModel


class FavoritsBase(BaseModel):
    id_business: str


class Favorits(FavoritsBase):
    id_favorits: str

    class Config:
        orm_mode = True


class FavoritsPaginated(BaseModel):
    results: list[Favorits]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
