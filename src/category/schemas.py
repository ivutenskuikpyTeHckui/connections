from typing import Optional

from pydantic import BaseModel


# Категории

class CreateCategoryModel(BaseModel):
    title: str


class UpdateCategoryModel(BaseModel):
    title: Optional[str] = None


# Подкатегории

class CreateSubcategoryModel(BaseModel):
    title:str 
    category_id:int

class UpdateSubcategoryModel(BaseModel):
    title: Optional[str] = None
    category_id: Optional[int] = None