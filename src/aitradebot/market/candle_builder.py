from dataclasses import dataclass
from datetime import datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle, Tick
from datetime import timedelta

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
        start = self._get_candle_start(tick.timestamp)

        self._current = _BuildingCandle(
            open=tick.price,
            high=tick.price,
            low=tick.price,
            close=tick.price,
            volume=tick.volume,
            start_time=start,
            end_time=start + timedelta(minutes=2),
        )

    def process(
        self,
        tick: Tick,
    ) -> list[Candle]:

        if self._current is None:
            self._start_new_candle(tick)
            return []

        if self._is_new_candle(tick):
            completed = self._build_completed_candle()

            self._start_new_candle(tick)

            return [completed]

        self._update_current_candle(tick)

        return []
    def _update_current_candle(
        self,
        tick: Tick,
    ) -> None:
        assert self._current is not None

        self._current.high = max(self._current.high, tick.price)
        self._current.low = min(self._current.low, tick.price)
        self._current.close = tick.price
        self._current.volume += tick.volume
        self._current.end_time = tick.timestamp
    def _get_candle_start(
        self,
        timestamp: datetime,
    ) -> datetime:
        ... 
    def _get_candle_start(
        self,
        timestamp: datetime,
    ) -> datetime:
        minute = timestamp.minute - (timestamp.minute % 2)

        return timestamp.replace(
            minute=minute,
            second=0,
            microsecond=0,
        )
    def _is_new_candle(
    self,
    tick: Tick,
    ) -> bool:
        assert self._current is not None

        return tick.timestamp >= self._current.end_time

    def _build_completed_candle(self) -> Candle:
        assert self._current is not None

        return Candle(
            instrument=self._instrument,
            timeframe=self._timeframe,
            open=self._current.open,
            high=self._current.high,
            low=self._current.low,
            close=self._current.close,
            volume=self._current.volume,
            start_time=self._current.start_time,
            end_time=self._current.end_time,
        )