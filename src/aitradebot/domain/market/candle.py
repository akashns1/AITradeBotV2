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

    @property
    def body_size(self) -> float:
        return abs(self.close - self.open)

    
    @property
    def range_size(self) -> float:
        return self.high - self.low

    @property
    def lower_wick_size(self) -> float:
        return min(self.open, self.close) - self.low

    @property
    def upper_wick_size(self) -> float:
        return self.high - max(self.open, self.close)

    @property
    def is_hammer(self) -> bool:
        return (
            self.is_bullish
            and self.lower_wick_size >= self.body_size * 2
            and self.upper_wick_size <= self.body_size
    )
    
    @property
    def is_strong_bullish(self) -> bool:
        return (
            self.is_bullish
            and self.range_size > 0
            and self.body_size / self.range_size > 0.5
        )