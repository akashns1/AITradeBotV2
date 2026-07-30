from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle


def make_candle(
    *,
    open: float = 100,
    high: float = 110,
    low: float = 99,
    close: float = 108,
    volume: int = 1000,
    instrument: Instrument | None = None,
    timeframe: TimeFrame = TimeFrame.TWO_MINUTES,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
) -> Candle:
    instrument = instrument or Instrument("NIFTY", "NSE")
    start_time = start_time or datetime.now(UTC)
    end_time = end_time or start_time

    return Candle(
        instrument=instrument,
        timeframe=timeframe,
        open=open,
        high=high,
        low=low,
        close=close,
        volume=volume,
        start_time=start_time,
        end_time=end_time,
    )