from aitradebot.domain.market import Candle
from aitradebot.trading.trade_decision_engine import TradeDecision


class StopLossCalculator:
    """
    Calculates the initial stop loss for a trade.
    """

    def calculate(
        self,
        decision: TradeDecision,
        candle: Candle,
    ) -> float:
        if decision.side == "LONG":
            return candle.low

        if decision.side == "SHORT":
            return candle.high

        raise ValueError(
            f"Unsupported trade side: {decision.side}"
        )   