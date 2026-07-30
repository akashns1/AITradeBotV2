from aitradebot.analysis.confirmation_analysis import ConfirmationAnalysis
from aitradebot.analysis.trend import Trend


class EntryConfirmation:
    def analyze(self, candles, trend: Trend) -> ConfirmationAnalysis:
        last_candle = candles[-1]

        if trend == Trend.UP and last_candle.is_bullish:
            return ConfirmationAnalysis(confirmed=True)

        return ConfirmationAnalysis(confirmed=False)