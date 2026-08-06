"""
Market Tick

Represents one market tick inside AITradeBot.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MarketTick:
    """
    Clean market tick independent of any broker.
    """

    security_id: str

    price: float

    timestamp: datetime