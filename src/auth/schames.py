from pydantic import BaseModel
from datetime import datetime

from fastapi_users import schemas


class CreateUser(BaseModel):
    email: str
    username: str
    last_name: str
    contacts: str
    address: str
    work_address: str
    status: str
    add_info: str
    user_info: str
    id_parent: int
    telegram_id: int    


# Авторизованные пользователи 


class UserRead(schemas.BaseUser[int]):
    id: int 
    username: str
    phone_number: str
    user_info: str
    hashed_password: str 
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    phone_number: str
    user_info: str
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserUpdate(schemas.BaseUserUpdate):
    pass
