import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from src.auth.models import Auth_user 
from src.auth.utils import get_user_db


from src.config import SECRET_MANAGER 


class UserManager(UUIDIDMixin, BaseUserManager[Auth_user, uuid.UUID]):
    reset_password_token_secret = SECRET_MANAGER
    verification_token_secret = SECRET_MANAGER

    async def on_after_register(self, user: Auth_user, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: Auth_user, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: Auth_user, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)