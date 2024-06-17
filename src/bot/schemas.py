from typing import Optional

from pydantic import BaseModel


class CreateUserBot(BaseModel):
    user_id:int
    friends_id:int
    friend_code:int
    username:str
    first_name:str


class UpdateUserBot(BaseModel):
    user_id:Optional[int] = None
    friends_id:Optional[int] = None
    friend_code:Optional[int] = None
    username:Optional[str] = None
    first_name:Optional[str] = None