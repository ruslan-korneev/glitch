from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.config.const import GITLAB_AUTH_URL
from src.utils.jwt import generate_jwt_token


def get_welcome_keyboard(user_id):
    welcome_keyboard = InlineKeyboardMarkup()
    state = generate_jwt_token(user_id)
    url = GITLAB_AUTH_URL.format(state=state)
    gitlab_bind_button = InlineKeyboardButton(
        text="bind gitlab",
        url=url,
        callback_data=f"gitlab-connect:{user_id}",
    )

    welcome_keyboard.add(gitlab_bind_button)

    return welcome_keyboard
