from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import auth, business, favoriteBusiness, product, user


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(auth.auth_router)
app.include_router(business.business_router)
app.include_router(product.product_router)
app.include_router(user.user_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
