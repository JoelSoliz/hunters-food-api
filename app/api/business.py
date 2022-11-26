from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.business import Business, BusinessCreate, BusinessPaginated
from schemas.product import ProductPaginated
from schemas.user import User
from schemas.favorite import FavoriteBusiness
from services.business import BusinessService
from services.product import ProductService
from services.favorite import FavoriteService


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


@business_router.post('/delete_favorite', tags=["Favorite"])
def delete_favorite_business(id_favorite, id_business, session: Session = Depends(get_db_session)):
    favorite_service = FavoriteService(session)
    business_service = BusinessService(session)
    get_favorite = favorite_service.get_favorite(id_favorite)
    get_business = business_service.get_business(id_business)
    if not get_favorite:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Favorite {id_favorite} not found. ")
    if not get_business:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product {id_business} not found. ")
    favorite_service.delete_favorite(id_favorite)
    return {"message": f"Favorite {id_favorite} successfully removed."}