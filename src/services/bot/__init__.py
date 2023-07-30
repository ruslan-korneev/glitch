from src.config.bot import bot, dispatcher

from .handlers import register_handlers

register_handlers(dispatcher)

__all__ = ["bot", "dispatcher"]
