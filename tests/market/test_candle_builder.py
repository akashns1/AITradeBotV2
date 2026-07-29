from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Tick
from aitradebot.market.candle_builder import CandleBuilder


def test_multiple_ticks_do_not_complete_candle() -> None:
    builder = CandleBuilder(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
    )

    tick1 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=25000,
        timestamp=datetime.now(UTC),
    )

    tick2 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=25010,
        timestamp=datetime.now(UTC),
    )

    assert builder.process(tick1) == []
    assert builder.process(tick2) == []


def test_multiple_ticks_do_not_emit_completed_candle() -> None:
    builder = CandleBuilder(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
    )

    tick1 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=25000,
        timestamp=datetime.now(UTC),
    )

    tick2 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=25010,
        timestamp=datetime.now(UTC),
        volume=5,
    )

    assert builder.process(tick1) == []
    assert builder.process(tick2) == []
