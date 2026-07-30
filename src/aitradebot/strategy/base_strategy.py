from abc import ABC, abstractmethod

from aitradebot.signals.signal import Signal
from aitradebot.strategy.market_context import MarketContext


class BaseStrategy(ABC):
    @abstractmethod
    def evaluate(
        self,
        context: MarketContext,
    ) -> Signal | None:
        """Evaluate the current market context."""
