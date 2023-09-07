from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config.const import DB_URI

engine = create_async_engine(DB_URI, future=True)
SessionLocal = async_sessionmaker(bind=engine)


class Base(DeclarativeBase):
    ...
