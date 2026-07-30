from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.signals import Signal, SignalType
from aitradebot.strategy.base_strategy import BaseStrategy
from aitradebot.strategy.engine import StrategyEngine
from aitradebot.strategy.market_context import MarketContext


class BuyStrategy(BaseStrategy):
    def evaluate(
        self,
        context: MarketContext,
    ) -> Signal | None:
        return Signal(
            signal_type=SignalType.BUY,
            instrument=context.candle.instrument,
            timeframe=context.candle.timeframe,
            timestamp=context.candle.end_time,
        )


def test_strategy_engine_returns_generated_signals() -> None:
    engine = StrategyEngine([BuyStrategy()])

    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=101,
        low=99,
        close=100,
        volume=100,
        start_time=datetime(2026, 1, 1, 9, 15, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    context = MarketContext(
        candle=candle,
        indicators={},
    )

    signals = engine.evaluate(context)

    assert len(signals) == 1
    assert signals[0].signal_type == SignalType.BUY
