from typing import Any

from aiogram.types import User as TgUser
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.decorators import include_session
from src.db.models.users import User


@include_session
async def get_or_create_user(session: AsyncSession, tg_user: TgUser, **_: Any) -> User:
    user = await User.get_by_pk(session, tg_user.id)
    if not user:
        user = User(
            telegram_id=tg_user.id,
            username=tg_user.username,
            first_name=tg_user.first_name,
            last_name=tg_user.last_name,
        )
        await user.save(session)
        await session.refresh(user)

        logger.info(f"User {user.telegram_id} saved")
    return user
