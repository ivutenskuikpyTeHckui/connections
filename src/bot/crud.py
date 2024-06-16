from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload, joinedload

from src.bot.models import Connect, User_bot

from src.database import async_session_maker


class UserBotRepository:
    @staticmethod
    async def get_all_users() -> list[User_bot]:
        async with async_session_maker() as session:
            query = (
                select(User_bot)
            )

            users = await session.scalars(query)
            await session.commit()

            return list(users)
