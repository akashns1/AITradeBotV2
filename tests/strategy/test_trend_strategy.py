from datetime import UTC, datetime

from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.analysis.trend import Trend
from aitradebot.analysis.trend_strength import TrendStrength
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.strategy.trend_strategy import TrendStrategy
from aitradebot.strategy.strategy_context import StrategyContext

def test_no_signal_for_weak_trend() -> None:
    strategy = TrendStrategy()

    analysis = MarketAnalysis(
        trend=Trend.UP,
        strength=TrendStrength.WEAK,
        ema_gap=1.0,
        atr=3.0,
    )

    context = StrategyContext(
        analysis=analysis,
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        timestamp=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    signal = strategy.evaluate(context)

    assert signal is None