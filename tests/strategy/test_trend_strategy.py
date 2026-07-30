from datetime import UTC, datetime

from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.analysis.trend import Trend
from aitradebot.analysis.trend_strength import TrendStrength
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.strategy.trend_strategy import TrendStrategy
from aitradebot.strategy.strategy_context import StrategyContext
from aitradebot.signals.signal_type import SignalType
from aitradebot.signals.signal import Signal
from aitradebot.analysis.pullback_analysis import PullbackAnalysis



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
        pullback=PullbackAnalysis(detected=True),
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        timestamp=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    signal = strategy.evaluate(context)

    assert signal is None
def test_buy_signal_for_strong_uptrend() -> None:
    strategy = TrendStrategy()

    analysis = MarketAnalysis(
        trend=Trend.UP,
        strength=TrendStrength.STRONG,
        ema_gap=1.0,
        atr=3.0,
    )

    context = StrategyContext(
        analysis=analysis,
        pullback=PullbackAnalysis(detected=True),
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        timestamp=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    signal = strategy.evaluate(context)

    assert signal is not None
    assert signal.signal_type == SignalType.BUY
    assert signal.instrument == context.instrument
    assert signal.timeframe == context.timeframe
    assert signal.timestamp == context.timestamp
def test_sell_signal_for_strong_downtrend() -> None:
    strategy = TrendStrategy()

    analysis = MarketAnalysis(
        trend=Trend.DOWN,
        strength=TrendStrength.STRONG,
        ema_gap=1.0,
        atr=3.0,
    )

    context = StrategyContext(
        analysis=analysis,
        pullback=PullbackAnalysis(detected=True),
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        timestamp=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    expected = Signal(
        signal_type=SignalType.SELL,
        instrument=context.instrument,
        timeframe=context.timeframe,
        timestamp=context.timestamp,
    )

    signal = strategy.evaluate(context)

    assert signal == expected
def test_no_signal_for_strong_uptrend_without_pullback():
    analysis = MarketAnalysis(
        trend=Trend.UP,
        strength=TrendStrength.STRONG,
        ema_gap=15.0,
        atr=20.0,
    )

    context = StrategyContext(
        analysis=analysis,
        pullback=PullbackAnalysis(detected=False),
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        timestamp=datetime.now(),
    )

    strategy = TrendStrategy()

    signal = strategy.evaluate(context)

    assert signal is None