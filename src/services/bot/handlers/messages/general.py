from aiogram import Dispatcher
from aiogram.types import Message


async def welcome(message: Message):
    user = message.from_user
    if user.is_bot:
        return

    await message.answer(
        r"Hey, {name}\! This is your id: `{user_id}`".format(
            name=(user.full_name or user.username), user_id=user.id
        )
    )


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(welcome, commands=["start"])
