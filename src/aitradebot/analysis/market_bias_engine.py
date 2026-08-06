from aitradebot.analysis.market_bias import MarketBias
from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.analysis.market_structure_analyzer import (
    MarketStructure,
)


class MarketBiasEngine:
    def analyze(
        self,
        structure: MarketStructure,
    ) -> MarketBias:

        if structure.is_bullish_bos:
            return MarketBias(
                direction=MarketDirection.BULLISH,
            )

        if structure.is_bearish_bos:
            return MarketBias(
                direction=MarketDirection.BEARISH,
            )

        return MarketBias(
            direction=MarketDirection.NEUTRAL,
        )