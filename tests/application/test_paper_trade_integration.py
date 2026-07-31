from aitradebot.application.bootstrap import create_application
from aitradebot.application.events.trade_decision_event import (
    TradeDecisionEvent,
)
from aitradebot.trading.trade_decision_engine import TradeDecision


def test_trade_decision_opens_paper_position(create_candle):
    app = create_application()

    decision = TradeDecision(
        action="BUY",
        side="LONG",
    )

    candle = create_candle(100)

    app.event_bus.publish(
        TradeDecisionEvent(
            decision=decision,
            candle=candle,
            stop_loss=98.0,
        )
    )

    assert app.paper_trade_engine.position is not None
    assert app.paper_trade_engine.position.side == "LONG"
    assert app.paper_trade_engine.position.entry_price == 100
    assert app.paper_trade_engine.position.stop_loss == 98.0