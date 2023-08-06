from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import User as TgUser
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.config.db import SessionLocal
from src.db.models import User
from src.services.bot.keyboards import get_welcome_keyboard


async def get_user(tg_id: int) -> User | None:
    async with SessionLocal() as db:
        query = select(User).filter(User.telegram_id == tg_id)
        result = await db.execute(query)
        try:
            user: User = result.scalar_one()
        except NoResultFound:
            return

        return user


async def create_user(tg_user: TgUser) -> User:
    async with SessionLocal() as db:
        user = User(
            telegram_id=tg_user.id,
            username=tg_user.username,
            first_name=tg_user.first_name,
            last_name=tg_user.last_name,
        )
        db.add(user)
        await db.commit()
        return user


async def get_or_create(tg_user: TgUser) -> User:
    user = await get_user(tg_user.id)
    if not user:
        user = await create_user(tg_user)

    return user

router = Router()


@router.message(Command("start"))
async def welcome(message: Message) -> None:
    tg_user = message.from_user
    if not tg_user or tg_user.is_bot:
        return

    user = await get_or_create(tg_user)

    keyboard = get_welcome_keyboard(tg_user.id)
    await message.answer(
        r"Welcome, {name}\! This is your id: `{user_id}`".format(
            name=(tg_user.full_name or tg_user.username), user_id=user.telegram_id
        ),
        reply_markup=keyboard,
    )
