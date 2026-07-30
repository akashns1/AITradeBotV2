from dataclasses import dataclass
from datetime import datetime

from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.analysis.pullback_analysis import PullbackAnalysis

@dataclass(frozen=True, slots=True)
class StrategyContext:
    analysis: MarketAnalysis
    pullback: PullbackAnalysis
    instrument: Instrument
    timeframe: TimeFrame
    timestamp: datetime