from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.exc import IntegrityError

from src.db import get_session
from src.db.models.users import User

from src.services.bot.keyboards import get_welcome_keyboard

router = Router()


@router.message(Command("start"))
async def welcome(message: Message) -> None:
    tg_user = message.from_user
    if not tg_user or tg_user.is_bot:
        return

    user = User(
        telegram_id=tg_user.id,
        username=tg_user.username,
        first_name=tg_user.first_name,
        last_name=tg_user.last_name,
    )
    async for session in get_session():
        try:
            user = await user.save(session)
        except IntegrityError:
            pass

    keyboard = get_welcome_keyboard(tg_user.id)
    msg_text = r"Welcome, {name}\! This is your id: `{user_id}`"
    await message.answer(
        msg_text.format(
            name=(tg_user.full_name or tg_user.username), user_id=user.telegram_id
        ),
        reply_markup=keyboard,
    )
