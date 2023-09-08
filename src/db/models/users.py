from typing import Any
from gitlab import Gitlab

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.config.redis import Redis

from src.db.models.base import CRUDModel
from src.services.gitlab.auth import get_access_token


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

    async def save_gitlab_token(
        self, access_token: str, refresh_token: str, oauth_code: str | None = None
    ) -> None:
        """Save gitlab access token"""
        redis = Redis(self)
        await redis.set("gitlab_access_token", access_token)
        await redis.set("gitlab_refresh_token", refresh_token)
        if oauth_code:
            await redis.set("gitlab_oauth_code", oauth_code)

    async def refresh_gitlab_token(self) -> str:
        """Refresh gitlab access token"""
        redis = Redis(self)
        refresh_token = await redis.get("gitlab_refresh_token")
        if not refresh_token:
            oauth_code = await redis.get("gitlab_oauth_code")
            if not oauth_code:
                # TODO: ask user to authorize again
                raise Exception
            response = get_access_token(oauth_code=oauth_code)
        else:
            response = get_access_token(refresh_token=refresh_token)
        await redis.set("gitlab_access_token", response["access_token"])
        await redis.set("gitlab_refresh_token", response["refresh_token"])
        return response["access_token"]

    async def get_gitlab_token(self) -> str:
        """Get gitlab access token"""
        redis = Redis(self)
        token = await redis.get("gitlab_access_token")
        if not token:
            token = await self.refresh_gitlab_token()

        return token

    @property
    async def gitlab(self) -> Gitlab:
        """Get gitlab instance with authenticated user"""
        access_token = await self.get_gitlab_token()
        gitlab = Gitlab(oauth_token=access_token)
        try:
            gitlab.auth()
        except Exception:
            access_token = await self.refresh_gitlab_token()
            gitlab = Gitlab(oauth_token=access_token)
            gitlab.auth()

        return gitlab
