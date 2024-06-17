from typing import Annotated

from fastapi import APIRouter, Query, Body

from src.bot.crud import UserBotRepository 
from src.bot.schemas import (
    CreateUserBot,
    UpdateUserBot
)


router = APIRouter(
    prefix="/bot",
    tags=["bot"]
)


@router.get("/get_all_users_bot")
async def get_all_users():
    query = await UserBotRepository.get_all_users()
    return query


@router.get("/get_user_bot")
async def get_user(user_id:Annotated[int, Query()]):
    query = await UserBotRepository.get_user_by_id(user_id)
    return query

@router.post("/add_user_bot")
async def add_user_bot(user_model:Annotated[CreateUserBot, Body()]):
    stmt = await UserBotRepository.add_user_bot(user_model)
    return stmt