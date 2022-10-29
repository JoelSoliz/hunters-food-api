from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from .dependencies import get_current_user, get_db_session
from schemas.product import Product, ProductBase, ProductPaginated, ProductUpdate
from schemas.user import User
from services.product import ProductService


product_router = APIRouter(prefix='/product')


@product_router.get('/', response_model=ProductPaginated)
def get_products(current_page: int, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    return product_service.get_products(current_page)


@product_router.post('/register', response_model=Product)
def add_product(product: ProductBase = Depends(), image: UploadFile = File(), session: Session = Depends(get_db_session), _: User = Depends(get_current_user)):
    product_service = ProductService(session)
    return product_service.register_product(product, image.file.read())


@product_router.get("/{id}/image")
def get_product_image(id, session: Session = Depends(get_db_session)):
    product_service = ProductService(session)
    product = product_service.get_product(id)
    if not product:
        return HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return Response(product.image, media_type="image/*")

@product_router.put('/{id}', response_model=Product)
def update_product(id:str, product: ProductUpdate=Depends(), session: Session = Depends(get_db_session), image: UploadFile = File()):
    product_service = ProductService(session)
    get_product = product_service.get_product(id)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts id {id} not found. ")  
    
    product_service.update_product(id, image.file.read(), product, get_product)  
    
    return get_product