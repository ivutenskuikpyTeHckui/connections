from typing import Optional

from pydantic import BaseModel


class Create_category_model(BaseModel):
    title: str


class Update_categoty__model(BaseModel):
    title: Optional[str] = None

