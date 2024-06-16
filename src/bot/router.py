from fastapi import APIRouter

from src.bot.crud import UserBotRepository 


router = APIRouter(
    prefix="/bot",
    tags=["bot"]
)


@router.get("/get_all_users")
async def get_all_users():
    query = await UserBotRepository.get_all_users()
    return query
