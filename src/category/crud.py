from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.category.models import Category, Subcategory

from src.database import async_session_maker

from src.category.schemas import Create_category_model


class CategoryRepository:
    @staticmethod
    async def add_category(category:Create_category_model)->Category:
        async with async_session_maker() as session:
            stmt = category.model_dump()
            new_category = Category(**stmt)
            session.add(new_category)
            await session.commit()

            return new_category
        
    @staticmethod
    async def get_categories() -> list[Category]:
        async with async_session_maker() as session:
           query = (
               select(Category).
               options(joinedload(Category.subcategory))
           )

           categories = await session.scalars(query)

           return list(categories)
