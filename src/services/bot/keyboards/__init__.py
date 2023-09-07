from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.config.const import GITLAB_AUTH_URL
from src.utils.jwt import generate_jwt_token


def get_welcome_keyboard(user_id: int) -> InlineKeyboardMarkup:
    state = generate_jwt_token(user_id)
    url = GITLAB_AUTH_URL.format(state=state)
    gitlab_bind_button = InlineKeyboardButton(
        text="bind gitlab",
        url=url,
        callback_data=f"gitlab-connect:{user_id}",
    )

    return InlineKeyboardMarkup(inline_keyboard=[[gitlab_bind_button]])
