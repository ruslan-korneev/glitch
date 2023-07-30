import click
from aiogram import asyncio
from loguru import logger

from src.services.bot import bot, dispatcher


async def _run_bot():
    try:
        logger.info("Bot Running")
        await dispatcher.start_polling()
    finally:
        await dispatcher.storage.close()
        await dispatcher.storage.wait_closed()
        session = await bot.get_session()
        if session:
            await session.close()


@click.command("bot")
def run_bot():
    """Run asynchronous telegram bot long polling."""
    asyncio.run(_run_bot())
