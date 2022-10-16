from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from api.dependencies import get_db_session
from schemas.business import Business, BusinessCreate
from services.business import BusinessService

business_router = APIRouter(prefix='/business')


@business_router.post('/register', response_model=Business)
def register_business(business: BusinessCreate = Depends() ,image_logo: UploadFile = File(), session: Session = Depends(get_db_session)):
    business_service = BusinessService(session)
    print(image_logo)
    print(business)
    return business_service.register_business(business, image_logo.file.read())
    #db_business = business_service.get_business_by_category(business.category)
    #print(db_business)

    #if db_business:
    #    raise HTTPException(status_code=400, detail="Email already registered")
