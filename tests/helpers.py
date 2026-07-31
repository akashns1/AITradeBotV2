from datetime import UTC, datetime

from aitradebot.domain.common.instrument import Instrument
from aitradebot.domain.market import Candle
from aitradebot.domain.common.timeframe import TimeFrame


def create_candle(close: float) -> Candle:
    return Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=close,
        high=close,
        low=close,
        close=close,
        volume=100,
        start_time=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 2, tzinfo=UTC),
    )