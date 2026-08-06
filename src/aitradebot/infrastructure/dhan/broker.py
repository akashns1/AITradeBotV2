"""
Dhan Broker

Thin wrapper around the Dhan SDK.
"""

from dhanhq import DhanContext, dhanhq

from aitradebot.config import (
    CLIENT_ID,
    ACCESS_TOKEN,
)


class Broker:

    def __init__(self) -> None:

        self._context = DhanContext(
            CLIENT_ID,
            ACCESS_TOKEN,
        )

        self._client = dhanhq(
            self._context,
        )

    @property
    def api(self):
        return self._client