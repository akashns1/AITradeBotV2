from dataclasses import dataclass
from datetime import datetime

from aitradebot.domain.common import Instrument, TimeFrame


@dataclass(frozen=True, slots=True)
class Candle:
    instrument: Instrument
    timeframe: TimeFrame

    open: float
    high: float
    low: float
    close: float

    volume: int

    start_time: datetime
    end_time: datetime

    @property
    def is_bullish(self) -> bool:
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open
