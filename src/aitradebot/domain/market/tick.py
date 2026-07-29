from dataclasses import dataclass
from datetime import datetime

from aitradebot.domain.common import Instrument


@dataclass(frozen=True, slots=True)
class Tick:
    instrument: Instrument
    price: float
    timestamp: datetime
    volume: int = 0

    def __post_init__(self) -> None:
        if self.price <= 0:
            raise ValueError("Price must be greater than zero.")

        if self.timestamp.tzinfo is None:
            raise ValueError("Timestamp must be timezone-aware.")
