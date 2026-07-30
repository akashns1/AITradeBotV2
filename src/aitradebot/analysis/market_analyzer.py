from aitradebot.analysis.market_analysis import MarketAnalysis
from aitradebot.analysis.trend import Trend
from aitradebot.analysis.trend_strength import TrendStrength
from aitradebot.strategy.market_context import MarketContext


class MarketAnalyzer:
    def analyze(
        self,
        context: MarketContext,
    ) -> MarketAnalysis:

        ema8 = context.indicators["EMA8"]
        ema20 = context.indicators["EMA20"]
        atr = context.indicators["ATR"]

        ema_gap = abs(ema8 - ema20)

        # Determine trend
        if ema8 > ema20:
            trend = Trend.UP
        elif ema8 < ema20:
            trend = Trend.DOWN
        else:
            trend = Trend.SIDEWAYS

        # Temporary strength classification
        if ema_gap >= atr:
            strength = TrendStrength.STRONG
        elif ema_gap >= atr * 0.5:
            strength = TrendStrength.MODERATE
        else:
            strength = TrendStrength.WEAK

        return MarketAnalysis(
            trend=trend,
            strength=strength,
            ema_gap=ema_gap,
            atr=atr,
        )