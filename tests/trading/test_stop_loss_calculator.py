from aitradebot.trading.stop_loss_calculator import (
    StopLossCalculator,
)
from aitradebot.trading.trade_decision_engine import (
    TradeDecision,
)


def test_long_stop_loss_uses_candle_low(create_candle):
    calculator = StopLossCalculator()

    candle = create_candle(100)

    decision = TradeDecision(
        action="BUY",
        side="LONG",
    )

    stop_loss = calculator.calculate(
        decision,
        candle,
    )

    assert stop_loss == candle.low


def test_short_stop_loss_uses_candle_high(create_candle):
    calculator = StopLossCalculator()

    candle = create_candle(100)

    decision = TradeDecision(
        action="SELL",
        side="SHORT",
    )

    stop_loss = calculator.calculate(
        decision,
        candle,
    )

    assert stop_loss == candle.high