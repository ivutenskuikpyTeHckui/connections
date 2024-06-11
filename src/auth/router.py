from typing import Annotated

from fastapi import APIRouter, Query, Body

from src.auth.crud import UserRepository

from src.auth.schames import CreateUser

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/create_user")
async def create_user(
    new_user: Annotated[CreateUser, Body()]
):
    new_user = await UserRepository.create_user(new_user)
    return new_user


@router.get("/get_all_users")
async def get_all_users():
    users = await UserRepository.get_all_users()
    return users
 
 
@router.get("/get_user")
async def get_user(user_id:int):
    user = await UserRepository.get_user(user_id)
    return user
    
# Авторизованные пользователи ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

@router.get("/get_all_auth_users")
async def get_all_auth_users():
    auth_users = await UserRepository.get_all_auth_users()
    return auth_users

@router.get("/get_auth_user")
async def get_auth_user(user_id:int):
    user = await UserRepository.get_auth_user(user_id)
    return user
