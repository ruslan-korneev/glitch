import asyncio

import click
from loguru import logger

from src.config.bot import bot, dispatcher


async def _run_bot():
    try:
        logger.info("Start Bot Long Polling")
        await dispatcher.start_polling(bot)
    finally:
        await dispatcher.storage.close()


@click.command("bot")
def run_bot():
    """Run asynchronous telegram bot long polling."""
    asyncio.run(_run_bot())
