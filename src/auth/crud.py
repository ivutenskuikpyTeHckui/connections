from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User

from src.database import async_session_maker

from src.auth.schames import (
    UserCreate,
    UserRead,
    UserUpdate
)

class UserRepository:

    @staticmethod
    async def get_all_users() -> list[User]:
        async with async_session_maker() as session:
            query = (
                select(User)
            )

            users = await session.scalars(query)

            return list(users)