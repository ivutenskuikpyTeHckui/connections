from datetime import datetime

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int 
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
    registered_at: datetime 
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
