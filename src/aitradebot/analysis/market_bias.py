from dataclasses import dataclass

from aitradebot.analysis.market_direction import MarketDirection


@dataclass(frozen=True, slots=True)
class MarketBias:
    direction: MarketDirection