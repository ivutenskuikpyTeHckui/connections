from typing import Annotated

from fastapi import APIRouter, Body

from src.category.crud import CategoryRepository
from src.category.schemas import (
    Create_category_model,
    Update_categoty__model
)


router = APIRouter(
    prefix="/category",
    tags=["category"]
)

# Роутеры для категорий 


@router.post("/add_category")
async def add_category(category:Annotated[Create_category_model, Body()]):
    category = await CategoryRepository.add_category(category)
    return category

@router.get("/get_categories")
async def get_categries():
    categories = await CategoryRepository.get_categories()
    return categories

@router.patch("/edit_category")
async def edit_category(
    category_id:Annotated[int, Body()], 
    updated_category:Annotated[Update_categoty__model, Body()]
):
    new_category = await CategoryRepository.edit_category(updated_category, category_id)
    return new_category

@router.delete("/delete_category")
async def delete_category(category_id:Annotated[int, Body()]):
    del_category = await CategoryRepository.delete_category(category_id)
    return del_category


# Роутеры для подкатегорий


