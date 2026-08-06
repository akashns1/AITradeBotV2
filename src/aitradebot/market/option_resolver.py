"""
Option Resolver

Resolves the broker instrument to trade.
"""

from aitradebot.infrastructure.dhan.instrument import BrokerInstrument
from aitradebot.infrastructure.dhan.instrument_repository import (
    InstrumentRepository,
)


class OptionResolver:

    def __init__(
        self,
        repository: InstrumentRepository,
    ) -> None:

        self._repository = repository

    # ---------------------------------------------------------

    def resolve(
        self,
        underlying: str,
        strike: int,
        option_type: str,
        expiry_date: str | None = None,
    ) -> BrokerInstrument:

        instrument = self._repository.get_option(
            underlying=underlying,
            strike=strike,
            option_type=option_type,
            expiry_date=expiry_date,
        )

        if instrument is None:
            raise RuntimeError(
                "Unable to resolve option "
                f"{underlying} "
                f"{strike} "
                f"{option_type}"
            )

        return instrument