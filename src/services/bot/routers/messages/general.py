from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def welcome(message: Message) -> None:
    user = message.from_user
    if not user or user.is_bot:
        return

    await message.answer(
        r"Hey, {name}\! This is your id: `{user_id}`".format(
            name=(user.full_name or user.username), user_id=user.id
        )
    )
