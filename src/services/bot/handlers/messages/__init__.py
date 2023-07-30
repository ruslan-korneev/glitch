from aiogram import Dispatcher

from .general import register_handlers as register_general_handlers


def register_message_handlers(dispatcher: Dispatcher):
    register_general_handlers(dispatcher)
