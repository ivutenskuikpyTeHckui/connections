from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User, App_User

from src.database import async_session_maker

from src.auth.schames import (
    UserCreate,
    UserRead,
    UserUpdate,
    CreateUser
)

class UserRepository:

    @staticmethod
    async def create_user(
        new_user: CreateUser,
    )->App_User:
        async with async_session_maker() as session:
            user = App_User(**new_user.model_dump(exclude_none=True))

            session.add(user)

            await session.commit()
            
            return user

    @staticmethod
    async def get_all_users() -> list[App_User]:
        async with async_session_maker() as session:
            query = (
                select(App_User)
            )

            users = await session.scalars(query)

            return list(users)
        
    @staticmethod
    async def get_user(user_id:int) -> App_User:
        async with async_session_maker() as session:
            query = (
                select(App_User).filter(App_User.id == user_id)
            )

            user = await session.scalar(query)

            return user
        
    @staticmethod
    async def get_user_by_parent_id(parent_id:int) -> list[User]:
        async with async_session_maker() as session:
            query = (
                select(App_User).filter(App_User.id_parent == parent_id)
            )

            user = await session.scalars(query)

            return list(user)
            
    @staticmethod
    async def get_all_auth_users() -> list[User]:
        async with async_session_maker() as session:
            query = (
                select(User)
            )

            auth_users = await session.scalars(query)

            return list(auth_users)
        
        
    @staticmethod
    async def get_auth_user(user_id:int) ->User:
        async with async_session_maker() as session:
            query = (
                select(User).filter(User.id == user_id)
            )

            auth_user = await session.scalar(query)

            return auth_user