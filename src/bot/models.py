from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User_bot(Base):
    __tablename__="user_bot"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=True)
    friends_id: Mapped[int] = mapped_column(nullable=True)
    friend_code: Mapped[int] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
