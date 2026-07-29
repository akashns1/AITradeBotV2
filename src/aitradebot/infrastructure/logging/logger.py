"""
Application logger wrapper.
"""

from logging import Logger as PythonLogger


class AppLogger:
    """
    Thin wrapper around Python's Logger.

    Keeps the rest of the application independent of the
    underlying logging implementation.
    """

    def __init__(self, logger: PythonLogger):
        self._logger = logger

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str) -> None:
        self._logger.error(message)

    def exception(self, message: str) -> None:
        self._logger.exception(message)
