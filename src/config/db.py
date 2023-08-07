from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.const import DB_URI

engine = create_async_engine(DB_URI, future=True)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)
Base = declarative_base()
