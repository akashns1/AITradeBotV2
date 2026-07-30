from collections.abc import Mapping
from dataclasses import dataclass

from aitradebot.domain.market import Candle


@dataclass(frozen=True, slots=True)
class MarketContext:
    candle: Candle
    indicators: Mapping[str, float]
