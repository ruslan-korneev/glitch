from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.const import DB_URI

engine = create_engine(DB_URI)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
