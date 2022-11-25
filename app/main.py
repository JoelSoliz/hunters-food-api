import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import auth, business, product, user


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


if __name__ == "__main__":
    port = os.getenv('PORT', default=8000)
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
