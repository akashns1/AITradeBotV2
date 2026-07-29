from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Tick
from aitradebot.market.candle_builder import CandleBuilder


def test_first_tick_returns_no_completed_candle() -> None:
    builder = CandleBuilder(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
    )

    tick = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=25000,
        timestamp=datetime.now(UTC),
    )

    assert builder.process(tick) == []
