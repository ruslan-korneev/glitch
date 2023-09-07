from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.config.db import Base, SessionLocal
from src.db import models

single_async_session: AsyncSession = SessionLocal()


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    async with SessionLocal() as session:
        yield session


__all__ = ["single_async_session", "Base", "models"]
