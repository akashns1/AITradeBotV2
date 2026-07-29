from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle


def test_bullish_candle() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=99,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.is_bullish
    assert not candle.is_bearish
