from dataclasses import dataclass

from aitradebot.analysis.trend import Trend
from aitradebot.analysis.trend_strength import TrendStrength


@dataclass(frozen=True, slots=True)
class MarketAnalysis:
    trend: Trend
    strength: TrendStrength
    ema_gap: float
    atr: float 