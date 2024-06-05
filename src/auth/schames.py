from datetime import datetime

from fastapi_users import schemas


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
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
