from fastapi import FastAPI

from api import auth, product


app = FastAPI()
app.include_router(auth.auth_router)
app.include_router(product.product_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
