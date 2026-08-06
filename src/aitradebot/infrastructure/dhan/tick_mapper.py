"""
Dhan Tick Mapper

Maps raw Dhan websocket ticks to domain Tick objects.
"""

from datetime import UTC, datetime

from aitradebot.domain.market import Tick
from aitradebot.domain.common import Instrument


class DhanTickMapper:
    """
    Maps raw Dhan websocket ticks to domain Tick objects.
    """

    def __init__(
        self,
        instruments: dict[str, Instrument],
    ) -> None:

        self._instruments = instruments

    # ---------------------------------------------------------

    def map(
        self,
        raw_tick: dict,
    ) -> Tick:

        if raw_tick.get("type") != "Ticker Data":
            raise ValueError(
                f"Unsupported tick type: "
                f"{raw_tick.get('type')}"
            )

        security_id = str(
            raw_tick["security_id"]
        )

        instrument = self._instruments.get(
            security_id
        )

        if instrument is None:
            raise ValueError(
                f"Unknown security id: {security_id}"
            )

        # Dhan sends only HH:MM:SS.
        # Until we receive the full trading date,
        # we combine it with today's UTC date.
        tick_time = datetime.strptime(
            raw_tick["LTT"],
            "%H:%M:%S",
        ).time()

        timestamp = datetime.combine(
            datetime.now(UTC).date(),
            tick_time,
            tzinfo=UTC,
        )

        return Tick(
            instrument=instrument,
            price=float(raw_tick["LTP"]),
            timestamp=timestamp,
            volume=0,
        )