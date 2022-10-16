from fastapi import FastAPI

from api import auth, user


app = FastAPI()
app.include_router(auth.auth_router)
app.include_router(user.user_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
