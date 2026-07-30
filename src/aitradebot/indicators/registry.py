from collections.abc import Iterator

from aitradebot.indicators import BaseIndicator


class IndicatorRegistry:
    def __init__(self) -> None:
        self._indicators: list[BaseIndicator] = []

    def register(
        self,
        indicator: BaseIndicator,
    ) -> None:
        self._indicators.append(indicator)

    def __iter__(self) -> Iterator[BaseIndicator]:
        return iter(self._indicators)

    def __len__(self) -> int:
        return len(self._indicators)
