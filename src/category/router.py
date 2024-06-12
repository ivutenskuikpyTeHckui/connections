from typing import Annotated

from fastapi import APIRouter, Body

from src.category.crud import CategoryRepository
from src.category.schemas import Create_category_model


router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.post("/add_category")
async def add_category(category:Annotated[Create_category_model, Body()]):
    category = await CategoryRepository.add_category(category)
    return category

@router.get("/get_categories")
async def get_categries():
    categories = await CategoryRepository.get_categories()
    return categories