from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from src.db.queries.users import get_or_create_user
from src.services.bot.keyboards import get_welcome_keyboard

router = Router()


@router.message(Command("start"))
async def welcome(message: Message) -> None:
    tg_user = message.from_user
    if not tg_user or tg_user.is_bot:
        return

    logger.debug(
        f"User {tg_user.id} | {tg_user.username or tg_user.first_name} connected"
    )

    user = await get_or_create_user(tg_user=tg_user)

    keyboard = get_welcome_keyboard(tg_user.id)
    msg_text = r"Welcome, {name}\! This is your id: `{user_id}`".format(
        name=(tg_user.full_name or tg_user.username), user_id=user.telegram_id
    )

    logger.debug(f"Message: {msg_text}")
    await message.answer(msg_text, reply_markup=keyboard)
