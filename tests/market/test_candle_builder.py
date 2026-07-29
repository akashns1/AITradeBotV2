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


def test_emits_completed_candle_on_timeframe_boundary() -> None:
    builder = CandleBuilder(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
    )

    tick1 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=100,
        timestamp=datetime(2026, 1, 1, 9, 14, 10, tzinfo=UTC),
    )

    tick2 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=105,
        timestamp=datetime(2026, 1, 1, 9, 15, 30, tzinfo=UTC),
    )

    tick3 = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=102,
        timestamp=datetime(2026, 1, 1, 9, 16, 0, tzinfo=UTC),
    )

    assert builder.process(tick1) == []
    assert builder.process(tick2) == []

    candles = builder.process(tick3)

    assert len(candles) == 1

    candle = candles[0]

    assert candle.open == 100
    assert candle.high == 105
    assert candle.low == 100
    assert candle.close == 105
