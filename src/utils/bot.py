from aiogram import Bot

from src.config.const import AIOGRAM_TOKEN


async def get_bot_username():
    bot = Bot(token=AIOGRAM_TOKEN)
    info = await bot.get_me()
    return info.username
