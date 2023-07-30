from aiogram import Bot, Dispatcher

from src.config.const import AIOGRAM_TOKEN

# About MarkdownV2: https://core.telegram.org/bots/api#markdownv2-style
bot = Bot(token=AIOGRAM_TOKEN, parse_mode="MarkdownV2")
dispatcher = Dispatcher(bot)

__all__ = ["bot", "dispatcher"]
