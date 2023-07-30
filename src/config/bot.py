from aiogram import Bot, Dispatcher

from src.config.const import AIOGRAM_TOKEN

bot = Bot(token=AIOGRAM_TOKEN)
dispatcher = Dispatcher(bot)
