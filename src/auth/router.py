from fastapi import APIRouter

from src.auth.crud import UserRepository


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.get("/users")
async def get_all_users():
    users = await UserRepository.get_all_users()
    return users
 
@router.get("/auth_users")
async def get_all_auth_users():
    auth_users = await UserRepository.get_all_auth_users()
    return auth_users


