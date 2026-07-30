from datetime import UTC, datetime

from aitradebot.application.events.candle_completed_event import CandleCompletedEvent
from aitradebot.application.events.event_bus import EventBus
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.indicators import BaseIndicator
from aitradebot.indicators.engine import IndicatorEngine
from aitradebot.indicators.registry import IndicatorRegistry


class DummyIndicator(BaseIndicator):
    def __init__(self) -> None:
        self.updated = False

    def update(self, candle: Candle) -> None:
        self.updated = True

    @property
    def value(self) -> float | None:
        return None


def test_indicator_engine_can_be_created() -> None:
    registry = IndicatorRegistry()

    engine = IndicatorEngine(registry)

    assert engine is not None


def test_engine_updates_registered_indicators() -> None:
    registry = IndicatorRegistry()

    indicator = DummyIndicator()

    registry.register(indicator)

    engine = IndicatorEngine(registry)

    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=95,
        close=105,
        volume=1000,
        start_time=datetime(2026, 1, 1, 9, 14, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 16, tzinfo=UTC),
    )

    engine.process(candle)

    assert indicator.updated


def test_engine_processes_candle_completed_event() -> None:
    registry = IndicatorRegistry()
    indicator = DummyIndicator()
    registry.register(indicator)

    event_bus = EventBus()
    engine = IndicatorEngine(registry)

    event_bus.subscribe(
        CandleCompletedEvent,
        engine.handle_candle_completed,
    )

    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=95,
        close=105,
        volume=1000,
        start_time=datetime(2026, 1, 1, 9, 14, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 16, tzinfo=UTC),
    )

    event_bus.publish(
        CandleCompletedEvent(candle=candle),
    )

    assert indicator.updated
