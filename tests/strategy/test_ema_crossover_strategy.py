from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.signals import SignalType
from aitradebot.strategy.ema_crossover_strategy import EMACrossoverStrategy
from aitradebot.strategy.market_context import MarketContext


def test_strategy_generates_buy_signal_on_bullish_crossover() -> None:
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
        indicators={
            "EMA20_PREV": 99.0,
            "EMA50_PREV": 100.0,
            "EMA20": 101.0,
            "EMA50": 100.0,
        },
    )

    strategy = EMACrossoverStrategy()

    signal = strategy.evaluate(context)

    assert signal is not None
    assert signal.signal_type == SignalType.BUY
