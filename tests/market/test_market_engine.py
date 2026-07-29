from datetime import UTC, datetime

from aitradebot.application.events.event_bus import EventBus
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Tick
from aitradebot.market.market_engine import MarketEngine


def test_market_engine_can_be_created() -> None:
    event_bus = EventBus()

    engine = MarketEngine(event_bus)

    assert engine is not None


def test_process_tick_returns_no_completed_candle_for_first_tick() -> None:
    event_bus = EventBus()

    engine = MarketEngine(event_bus)

    instrument = Instrument("NIFTY", "NSE")

    engine.add_instrument(
        instrument=instrument,
        timeframe=TimeFrame.TWO_MINUTES,
    )

    tick = Tick(
        instrument=instrument,
        price=25000,
        timestamp=datetime.now(UTC),
    )

    assert engine.process_tick(tick) == []