from fastapi import FastAPI

from api import auth


app = FastAPI()
app.include_router(auth.auth_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
