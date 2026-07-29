from datetime import UTC, datetime

from aitradebot.application.events import CandleCompletedEvent
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


def test_completed_candle_publishes_event() -> None:
    event_bus = EventBus()

    received_events: list[CandleCompletedEvent] = []

    def handler(event: CandleCompletedEvent) -> None:
        received_events.append(event)

    event_bus.subscribe(CandleCompletedEvent, handler)

    engine = MarketEngine(event_bus)

    instrument = Instrument("NIFTY", "NSE")

    engine.add_instrument(
        instrument=instrument,
        timeframe=TimeFrame.TWO_MINUTES,
    )

    ticks = [
        Tick(
            instrument=instrument,
            price=25000,
            timestamp=datetime(2026, 1, 1, 9, 14, 10, tzinfo=UTC),
        ),
        Tick(
            instrument=instrument,
            price=25010,
            timestamp=datetime(2026, 1, 1, 9, 15, 30, tzinfo=UTC),
        ),
        Tick(
            instrument=instrument,
            price=25020,
            timestamp=datetime(2026, 1, 1, 9, 16, 0, tzinfo=UTC),
        ),
    ]

    for tick in ticks:
        engine.process_tick(tick)

    assert len(received_events) == 1
    assert received_events[0].candle.close == 25010
