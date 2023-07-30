from aiogram import Dispatcher
from loguru import logger

from .messages import register_message_handlers


def register_handlers(dispatcher: Dispatcher) -> None:
    logger.debug("Setting up Bot Handlers ...")
    register_message_handlers(dispatcher)
