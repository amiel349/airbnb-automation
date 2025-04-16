import os
import sys
from loguru import logger


class Logger:
    """Logger class for logging messages"""

    def __init__(self):
        log_level = os.getenv("LOG_LEVEL", "INFO")
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        )

        # Configure logger
        logger.remove()  # Remove default handler
        logger.add(
            sys.stdout,
            format=log_format,
            level=log_level,
            colorize=True,
        )
        logger.add(
            "logs/airbnb_tests.log",
            format=log_format,
            level=log_level,
            rotation="10 MB",
            retention="1 week",
        )

    def get_logger(self):
        """Get the configured logger"""
        return logger