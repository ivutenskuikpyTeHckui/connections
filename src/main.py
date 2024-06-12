from fastapi import FastAPI


from fastapi_users import FastAPIUsers


from src.auth.models import User
from src.auth.router import router as router_auth
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schames import UserCreate, UserRead

from src.category.router import router as router_category



app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_auth)
app.include_router(router_category)