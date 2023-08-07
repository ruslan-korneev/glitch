from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.config.db import Base, SessionLocal
from src.db import models

db: AsyncSession = SessionLocal()

__all__ = ["db", "Base", "models"]
