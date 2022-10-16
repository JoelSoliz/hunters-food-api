from fastapi import FastAPI

from api import auth, product, business


app = FastAPI()
app.include_router(auth.auth_router)
app.include_router(product.product_router)
app.include_router(business.business_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
