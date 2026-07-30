from datetime import datetime

from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.analysis.trend_strength import TrendStrength
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.signals.signal import Signal
from aitradebot.strategy.strategy_context import StrategyContext
from aitradebot.analysis.trend import Trend
from aitradebot.signals.signal import Signal
from aitradebot.signals.signal_type import SignalType

class TrendStrategy:
     def evaluate(
        self,
        context: StrategyContext,
    ) -> Signal | None:

        if context.analysis.strength == TrendStrength.WEAK:
            return None
        if not context.pullback.detected:
            return None
        
        if (
            context.analysis.trend == Trend.UP
            and context.analysis.strength == TrendStrength.STRONG
        ):
            return Signal(
            signal_type=SignalType.BUY,
            instrument=context.instrument,
            timeframe=context.timeframe,
            timestamp=context.timestamp,
        )
        if (
            context.analysis.trend == Trend.DOWN
            and context.analysis.strength == TrendStrength.STRONG
        ):
            return Signal(
                signal_type=SignalType.SELL,
                instrument=context.instrument,
                timeframe=context.timeframe,
                timestamp=context.timestamp,
            )
        raise NotImplementedError