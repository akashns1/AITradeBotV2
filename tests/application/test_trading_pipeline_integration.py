from unittest.mock import MagicMock

from aitradebot.application.bootstrap import create_application
from aitradebot.application.events.candle_completed_event import (
    CandleCompletedEvent,
)
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from datetime import UTC, datetime


def test_pipeline_receives_candle_completed_event():
    app = create_application()

    app.trading_pipeline.handle_candle_completed = MagicMock()

    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=105,
        low=99,
        close=104,
        volume=100,
        start_time=datetime(2026, 1, 1, 9, 15, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    app.event_bus.publish(
        CandleCompletedEvent(candle=candle)
    )

    assert "Decision=" in captured.out