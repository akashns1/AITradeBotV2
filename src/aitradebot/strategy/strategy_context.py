from dataclasses import dataclass
from datetime import datetime

from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.domain.common import Instrument, TimeFrame


@dataclass(frozen=True, slots=True)
class StrategyContext:
    analysis: MarketAnalysis
    instrument: Instrument
    timeframe: TimeFrame
    timestamp: datetime