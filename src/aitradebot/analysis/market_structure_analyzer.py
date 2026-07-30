from dataclasses import dataclass

from aitradebot.analysis.swing_detector import SwingAnalysis


@dataclass(frozen=True) 
class MarketStructure:
    is_higher_high: bool
    is_higher_low: bool
    is_lower_high: bool
    is_lower_low: bool
    is_bullish_bos: bool
    is_bearish_bos: bool


class MarketStructureAnalyzer:
    def analyze(self, analysis: SwingAnalysis) -> MarketStructure:
        latest_high = analysis.latest_high
        previous_high = analysis.previous_high

        is_higher_high = (
            latest_high is not None
            and previous_high is not None
            and latest_high.price > previous_high.price
        )

        is_lower_high = (
            latest_high is not None
            and previous_high is not None
            and latest_high.price < previous_high.price
        )
        latest_low = analysis.latest_low
        previous_low = analysis.previous_low

        is_higher_low = (
            latest_low is not None
            and previous_low is not None
            and latest_low.price > previous_low.price
        )
        is_lower_low = (
            latest_low is not None
            and previous_low is not None
            and latest_low.price < previous_low.price
        )
        is_bullish_bos = (
            is_higher_high
            and is_higher_low
        )

        is_bearish_bos = (
            is_lower_high
            and is_lower_low
        )
    
        return MarketStructure(
            is_higher_high=is_higher_high,
            is_higher_low=is_higher_low,
            is_lower_high=is_lower_high,
            is_lower_low=is_lower_low,
            is_bullish_bos=is_bullish_bos,
            is_bearish_bos=is_bearish_bos,
        )