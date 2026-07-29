"""
Logger factory.
"""

import logging
from pathlib import Path

from aitradebot.infrastructure.logging.formatter import create_formatter
from aitradebot.infrastructure.logging.logger import AppLogger

_LOG_DIRECTORY = Path("logs")


class LoggerFactory:
    """
    Creates configured application loggers.
    """

    @staticmethod
    def get_logger(name: str) -> AppLogger:

        _LOG_DIRECTORY.mkdir(exist_ok=True)

        logger = logging.getLogger(name)

        if logger.handlers:
            return AppLogger(logger)

        logger.setLevel(logging.INFO)

        formatter = create_formatter()

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logfile = logging.FileHandler(
            _LOG_DIRECTORY / "aitradebot.log",
            encoding="utf-8",
        )
        logfile.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(logfile)

        return AppLogger(logger)
