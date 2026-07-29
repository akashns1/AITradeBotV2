"""
Logging formatter configuration.
"""

from logging import Formatter

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def create_formatter() -> Formatter:
    """
    Create the application's standard log formatter.
    """
    return Formatter(LOG_FORMAT, DATE_FORMAT)