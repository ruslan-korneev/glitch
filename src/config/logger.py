from datetime import time

from loguru import logger

from src.config.const import DEBUG, LOG_DIR


def configure_logger():
    logger.add(
        LOG_DIR.joinpath("{time:%Y-%m-%d}.logs"),
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{message}</level>",
        level="DEBUG" if DEBUG else "INFO",
        rotation=time(0, 0, 0),
        retention=30,  # каждый 1 день создается 1 файл
        delay=True,
        backtrace=True,
        diagnose=DEBUG,
        colorize=True,
        serialize=True,
    )
