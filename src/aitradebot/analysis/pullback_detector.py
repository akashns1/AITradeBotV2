from aitradebot.analysis.pullback_analysis import PullbackAnalysis
from aitradebot.analysis.trend import Trend


class PullbackDetector:
    def analyze(self, candles, trend: Trend) -> PullbackAnalysis:
        last_candle = candles[-1]

        if trend == Trend.UP and last_candle.is_bearish:
            return PullbackAnalysis(detected=True)

        if trend == Trend.DOWN and last_candle.is_bullish:
            return PullbackAnalysis(detected=True)

        return PullbackAnalysis(detected=False)