from fastapi import FastAPI
from controller.auth_controller import auth_router


app = FastAPI()


app.include_router(auth_router, prefix="/api/v1/auth")
