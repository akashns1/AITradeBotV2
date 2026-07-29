from abc import ABC, abstractmethod

from aitradebot.domain.market import Candle


class BaseIndicator(ABC):
    @abstractmethod
    def update(
        self,
        candle: Candle,
    ) -> None:
        """Update the indicator using a completed candle."""

    @property
    @abstractmethod
    def value(self) -> float | None:
        """Return the latest indicator value."""
