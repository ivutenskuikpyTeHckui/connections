from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload, joinedload

from src.category.models import Category, Subcategory

from src.database import async_session_maker

from src.category.schemas import (
    CreateCategoryModel,
    UpdateCategoryModel, 
    CreateSubcategoryModel,
    UpdateSubcategoryModel,
)


class CategoryRepository:
    @staticmethod
    async def add_category(category:CreateCategoryModel)->Category:
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
        updated_category:UpdateCategoryModel,
        category_id:int,
    ) -> Category:
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
        

class SubcategoryRepository:
    @staticmethod
    async def add_subcategory(
        subcategory:CreateSubcategoryModel,
    ) -> Subcategory:
        async with async_session_maker() as session:
            stmt = subcategory.model_dump()
            new_subcategory = Subcategory(**stmt)
            session.add(new_subcategory)
            await session.commit()

            return new_subcategory
    
    @staticmethod
    async def get_subcategories() -> list[Subcategory]:
        async with async_session_maker() as session:
            query = (
                select(Subcategory)
            )

            subcategories = await session.scalars(query)
            await session.commit()
            return list(subcategories)
        
    @staticmethod
    async def get_subcategory(subcategory_id:int) -> Subcategory:
        async with async_session_maker() as session:
            query = (
                select(Subcategory).
                filter(Subcategory.id == subcategory_id)
            )

            subcategory = await session.scalar(query)
            await session.commit()
            return subcategory
        
    @staticmethod
    async def edit_subcategory(
        updated_subcategory: UpdateSubcategoryModel,
        subcategory_id: int,
    ):
        async with async_session_maker() as session:
            stmt = (
                update(Subcategory).
                filter(Subcategory.id == subcategory_id).
                values(**updated_subcategory.model_dump(exclude_none=True))
            ).returning(Subcategory)

            subcategory = await session.scalar(stmt)
            await session.commit()
            return subcategory
        
    @staticmethod
    async def delete_subcategory(subcategory_id:int):
        async with async_session_maker() as session:
            stmt = (
                delete(Subcategory).
                filter(Subcategory.id == subcategory_id)
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}
