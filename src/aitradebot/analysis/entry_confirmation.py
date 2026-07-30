from aitradebot.analysis.confirmation_analysis import ConfirmationAnalysis
from aitradebot.analysis.pullback_analysis import PullbackAnalysis
from aitradebot.analysis.trend import Trend


class EntryConfirmation:
    def analyze(
        self,
        candles,
        trend: Trend,
        pullback: PullbackAnalysis,
    ) -> ConfirmationAnalysis:

        # NEW RULE
        if not pullback.detected:
            return ConfirmationAnalysis(confirmed=False)

        last_candle = candles[-1]

        if trend == Trend.UP and last_candle.is_strong_bullish:
            return ConfirmationAnalysis(confirmed=True)

        return ConfirmationAnalysis(confirmed=False)