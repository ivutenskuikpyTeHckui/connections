from typing import Annotated

from fastapi import APIRouter, Query, Body

from src.bot.crud import UserBotRepository 


router = APIRouter(
    prefix="/bot",
    tags=["bot"]
)


@router.get("/get_all_users")
async def get_all_users():
    query = await UserBotRepository.get_all_users()
    return query


@router.get("/get_user")
async def get_user(user_id:Annotated[int, Query()]):
    query = await UserBotRepository.get_user_by_id(user_id)
    return query