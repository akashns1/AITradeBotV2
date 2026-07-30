from aitradebot.analysis.pullback_analysis import PullbackAnalysis
from aitradebot.analysis.trend import Trend


class PullbackDetector:
    def analyze(self, candles, trend: Trend) -> PullbackAnalysis:
        if trend == Trend.UP and candles[-1].is_bearish:
            return PullbackAnalysis(detected=True)

        return PullbackAnalysis(detected=False)