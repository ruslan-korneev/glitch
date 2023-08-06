from typing import Any

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models.base import CRUDModel


class User(CRUDModel):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=False
    )
    gitlab_profile_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True)
    first_name: Mapped[str | None] = mapped_column(String(64), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(64), nullable=True)

    def __init__(
        self,
        *,
        telegram_id: int,
        gitlab_profile_id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        **kw: Any
    ) -> None:
        self.telegram_id = telegram_id
        self.gitlab_profile_id = gitlab_profile_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        return super().__init__(**kw)
