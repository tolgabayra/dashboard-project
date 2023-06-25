from fastapi import APIRouter
from schema.user_schema import LoginUser, CreateUser
from service.auth_service import AuthService

auth_router = APIRouter()


@auth_router.post("/login")
async def login(user: LoginUser, status_code=201):
    pass


@auth_router.post("/register")
async def register(user: CreateUser):
    pass

