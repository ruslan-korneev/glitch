from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.config.const import AIOGRAM_TOKEN
from src.services.bot.routers import router

bot = Bot(token=AIOGRAM_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)
dispatcher = Dispatcher()
dispatcher.include_router(router)

__all__ = ["bot", "dispatcher"]
