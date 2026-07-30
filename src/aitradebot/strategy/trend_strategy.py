from datetime import datetime

from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.analysis.trend_strength import TrendStrength
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.signals.signal import Signal
from aitradebot.strategy.strategy_context import StrategyContext

class TrendStrategy:
     def evaluate(
        self,
        context: StrategyContext,
    ) -> Signal | None:

        if context.analysis.strength == TrendStrength.WEAK:
            return None

        raise NotImplementedError