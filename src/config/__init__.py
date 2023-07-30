from src.config.bot import bot, dispatcher
from src.config.db import db
from src.config.logger import configure_logger  # noqa[#F401]

configure_logger()

__all__ = [
    "bot",
    "dispatcher",
    "db",
]
