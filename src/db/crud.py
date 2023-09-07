from typing import Sequence

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.exceptions import NotFoundConstraintError
from src.db.models import User


async def create_user(session: AsyncSession, user_id: int, **kwargs) -> User:
    user = User(telegram_id=user_id, **kwargs)
    session.add(user)
    await session.commit()
    return user


async def get_users(session: AsyncSession) -> Sequence[User]:
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    query = select(User).where(User.telegram_id == user_id)
    result = await session.execute(query)
    return result.scalar_one()


async def update_user(session: AsyncSession, user_id: int, **kwargs) -> User:
    user = await get_user_by_id(session, user_id)

    if user is None:
        raise NotFoundConstraintError(f"User with ID {id} not found.")

    for key, value in kwargs.items():
        setattr(user, key, value)

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(session: AsyncSession, user_id: int) -> None:
    query = delete(User).filter(User.telegram_id == user_id)
    await session.execute(query)
    await session.commit()
