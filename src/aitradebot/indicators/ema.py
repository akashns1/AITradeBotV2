from aitradebot.domain.market import Candle
from aitradebot.indicators import BaseIndicator


class EMA(BaseIndicator):
    def __init__(
        self,
        period: int,
    ) -> None:
        self._period = period
        self._value: float | None = None
        self._closes: list[float] = []

    @property
    def period(self) -> int:
        return self._period

    @property
    def value(self) -> float | None:
        return self._value

    def update(
        self,
        candle: Candle,
    ) -> None:
        self._closes.append(candle.close)

        if len(self._closes) < self._period:
            return

        if self._value is None:
            self._value = sum(self._closes[-self._period :]) / self._period
            return

        multiplier = 2 / (self._period + 1)

        self._value = candle.close * multiplier + self._value * (1 - multiplier)
