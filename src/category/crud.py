from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.category.models import Category, Subcategory

from src.database import async_session_maker

from src.category.schemas import (
    Create_category_model,
    Update_categoty__model
)


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
           await session.commit()

           return list(categories)
    
    @staticmethod
    async def get_category(category_id:int) -> Category:
        async with async_session_maker() as session:
            query = (
                select(Category).
                filter(Category.id == category_id)
            )

            category = await session.scalar(query)
            await session.commit()

            return category

    @staticmethod
    async def edit_category(
        updated_category:Update_categoty__model,
        category_id:int,
    )-> Category:
        async with async_session_maker() as session:
            stmt = (
                update(Category).
                filter(Category.id == category_id).
                values(**updated_category.model_dump(exclude_none=True))
            ).returning(Category)

            category = await session.scalar(stmt)
            await session.commit()
            
            return category
        
    @staticmethod
    async def delete_category(category_id:int):
        async with async_session_maker() as session:
            stmt = (
                delete(Category).
                filter(Category.id == category_id)
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}