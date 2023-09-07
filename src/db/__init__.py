from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.config.db import Base, SessionLocal
from src.db import models


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()


__all__ = ["Base", "models", "get_session"]
