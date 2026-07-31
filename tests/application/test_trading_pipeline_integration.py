from datetime import UTC, datetime

from aitradebot.application.bootstrap import create_application
from aitradebot.application.events import (
    CandleCompletedEvent,
    TradeDecisionEvent,
)
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.trading.trade_decision_engine import TradeDecision

def test_pipeline_publishes_trade_decision_event():
    app = create_application()

    app.trading_pipeline.process = lambda candles: TradeDecision(
        action="BUY",
        side="LONG",
    )

    received = []

    def handler(event: TradeDecisionEvent):
        received.append(event)

    app.event_bus.subscribe(
        TradeDecisionEvent,
        handler,
    )

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
        CandleCompletedEvent(
            candle=candle,
        )
    )

    assert len(received) == 1
    assert received[0].decision.side == "LONG"