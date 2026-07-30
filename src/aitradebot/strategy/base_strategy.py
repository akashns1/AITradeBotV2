from abc import ABC, abstractmethod

from aitradebot.domain.market import Candle
from aitradebot.signals.signal import Signal


class BaseStrategy(ABC):
    @abstractmethod
    def evaluate(
        self,
        candle: Candle,
    ) -> Signal | None:
        """Evaluate the latest candle and return a signal."""
