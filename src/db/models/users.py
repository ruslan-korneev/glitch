from sqlalchemy import Column, SmallInteger, String

from src.config.db import Base


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(SmallInteger, primary_key=True, autoincrement=False)
    gitlab_profile_id = Column(SmallInteger, nullable=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
