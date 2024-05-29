from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

# if TYPE_CHECKING:


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    contacts: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=True)
    work_address: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=False)
    add_info: Mapped[str] = mapped_column(nullable=True)
    user_info: Mapped[str] = mapped_column(nullable=True)
    id_parent: Mapped[int] = mapped_column(nullable=True)
    telegram_id: Mapped[int] = mapped_column(nullable=False)
    registered_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    is_active: Mapped[bool] = mapped_column( default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    

