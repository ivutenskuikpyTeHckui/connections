from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.category.crud import (
    CategoryRepository, 
    SubcategoryRepository,
)
from src.category.schemas import (
    CreateCategoryModel,
    UpdateCategoryModel,
    CreateSubcategoryModel,
    UpdateSubcategoryModel,
)


router = APIRouter(
    prefix="/category",
    tags=["category"]
)

# Роутеры для категорий 


@router.post("/add_category")
async def add_category(category_model:Annotated[CreateCategoryModel, Body()]):
    category = await CategoryRepository.add_category(category_model)
    return category

@router.get("/get_categories")
async def get_categories():
    categories = await CategoryRepository.get_categories()
    return categories

@router.get("/get_category")
async def get_category(category_id:Annotated[int, Query()]):
    category = await CategoryRepository.get_category(category_id)
    return category

@router.patch("/edit_category")
async def edit_category(
    category_id:Annotated[int, Body()], 
    updated_category:Annotated[UpdateCategoryModel, Body()]
):
    new_category = await CategoryRepository.edit_category(updated_category, category_id)
    return new_category

@router.delete("/delete_category")
async def delete_category(category_id:Annotated[int, Body()]):
    del_category = await CategoryRepository.delete_category(category_id)
    return del_category


# Роутеры для подкатегорий

@router.post("/add_subcategory")
async def add_subcategory(
    subcategory_model:Annotated[CreateSubcategoryModel, Body()],
):
    subcategory = await SubcategoryRepository.add_subcategory(subcategory_model)
    return subcategory

@router.get("/get_subcategories")
async def get_subcategories():
    subcategories = await SubcategoryRepository.get_subcategories()
    return subcategories

@router.get("/get_subcategory")
async def get_subcategory(subcategory_id:Annotated[int, Query()]):
    subcategory = await SubcategoryRepository.get_subcategory(subcategory_id)
    return subcategory

@router.patch("/edit_subcategory")
async def edit_subcategory(
    subcategory_id:Annotated[int, Body()], 
    updated_subcategory:Annotated[UpdateSubcategoryModel, Body()]
):
    new_subcategory = await SubcategoryRepository.edit_subcategory(updated_subcategory, subcategory_id)
    return new_subcategory

@router.delete("/delete_subcategory")
async def delete_subcategory(subcategory_id:Annotated[int, Body()]):
    del_subcategory = await SubcategoryRepository.delete_subcategory(subcategory_id)
    return del_subcategory

