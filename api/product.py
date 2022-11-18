from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from services.business import BusinessService

from .dependencies import get_current_user, get_db_session
from schemas.product import Product, ProductBase, ProductPaginated
from schemas.user import User
from services.product import ProductService


product_router = APIRouter(prefix='/product')


@product_router.get('/', response_model=ProductPaginated, tags=["Product"])
def get_products(current_page: int, session: Session = Depends(get_db_session), product_type=None, name_similar=None):
    product_service = ProductService(session)
    return product_service.get_products(current_page, product_type=product_type, name=name_similar)


@product_router.get("/{id}", response_model=Product, tags=["Product"])
def get_product(id, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    product = product_service.get_product(id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@product_router.get("/{id}/image", tags=["Product"])
def get_product_image(id, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    product = product_service.get_product(id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return Response(product.image, media_type="image/*")


@product_router.post('/register', response_model=Product, tags=["Product"])
def add_product(
    product: ProductBase = Depends(),
    image: UploadFile = File(default=None),
    session: Session = Depends(get_db_session),
    _: User = Depends(get_current_user)
):
    product_service = ProductService(session)
    if image:
        image = image.file.read()

    return product_service.register_product(product, image)


@product_router.put('/{id}', response_model=Product, tags=["Product"])
def update_product(
    id: str,
    product: ProductBase = Depends(),
    session: Session = Depends(get_db_session),
    image: UploadFile = File(default=None),
    user: User = Depends(get_current_user)
):
    product_service = ProductService(session)
    business_service = BusinessService(session)
    get_product = product_service.get_product(id)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"posts id {id} not found. ")

    if not business_service.check_business_by_user(
            user.id_user, get_product.id_business):
        raise HTTPException(status_code=401)

    if image:
        image = image.file.read()

    product_service.update_product(id, image, product, get_product)
    return get_product
