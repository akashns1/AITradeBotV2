from dataclasses import dataclass
from datetime import datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle, Tick


@dataclass(slots=True)
class _BuildingCandle:
    open: float
    high: float
    low: float
    close: float
    volume: int

    start_time: datetime
    end_time: datetime


class CandleBuilder:
    def __init__(
        self,
        instrument: Instrument,
        timeframe: TimeFrame,
    ) -> None:
        self._instrument = instrument
        self._timeframe = timeframe
        self._current: _BuildingCandle | None = None

    def _start_new_candle(
        self,
        tick: Tick,
    ) -> None:
        self._current = _BuildingCandle(
            open=tick.price,
            high=tick.price,
            low=tick.price,
            close=tick.price,
            volume=tick.volume,
            start_time=tick.timestamp,
            end_time=tick.timestamp,
        )

    def process(
        self,
        tick: Tick,
    ) -> list[Candle]:
        if self._current is None:
            self._start_new_candle(tick)
            return []

        return []
