from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.business import Business, BusinessCreate, BusinessPaginated
from schemas.favorite import FavoriteBusiness
from schemas.product import ProductPaginated
from schemas.user import User
from services.business import BusinessService
from services.favorite import FavoriteService
from services.product import ProductService


business_router = APIRouter(prefix='/business')


@business_router.get('/', response_model=BusinessPaginated, tags=["Business"])
def get_businesses(current_page: int, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    return business_service.get_businesses(current_page)


@business_router.get("/{id}", response_model=Business, tags=["Business"])
def get_business(id: str, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    business = business_service.get_business(id)
    if not business:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"posts id {id} not found. ")
    return business


@business_router.get("/{id}/image", tags=["Business"])
def get_business_image(id, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    business = business_service.get_business(id)
    if not business:
        raise HTTPException(
            status_code=404,
            detail="Business not found"
        )

    return Response(business.logo, media_type="image/*")


@business_router.get("/{id}/products", response_model=ProductPaginated, tags=["Business", "Product"])
def get_products_by_business(id: str, current_page: int, session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    business = business_service.get_business(id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found.")

    product_service = ProductService(session)
    return product_service.get_products(current_page, business=id)


@business_router.post('/register', response_model=Business, tags=["Business"])
def register_business(business: BusinessCreate = Depends(), image_logo: UploadFile = File(), session: Session = Depends(get_db_session), user: User = Depends(get_current_user)):
    business_service = BusinessService(session)
    return business_service.register_business(user.id_user, business, image_logo.file.read())


@business_router.post('/add_favorite', response_model=FavoriteBusiness, tags=["Favorite"])
def add_favorite_business(id_business,
                          session: Session = Depends(get_db_session),
                          user: User = Depends(get_current_user)
                          ):
    favorite_service = FavoriteService(session)
    favorite_business = favorite_service.add_favorite_business(
        user.id_user, id_business)
    return favorite_business


@business_router.delete('/favorite/{id}', tags=["Favorite"])
def delete_favorite_business(id, session: Session = Depends(get_db_session), user: User = Depends(get_current_user)):
    favorite_service = FavoriteService(session)
    get_favorite = favorite_service.get_favorite(id, user.id_user)
    if not get_favorite:
        raise HTTPException(status_code=403,
                            detail=f"{id} does not have permission. ")
    favorite_service.delete_favorite(id)
    return {"message": f"Favorite {id} successfully removed."}
