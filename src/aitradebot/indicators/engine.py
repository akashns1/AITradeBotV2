from aitradebot.application.events.candle_completed_event import (
    CandleCompletedEvent,
)
from aitradebot.domain.market import Candle
from aitradebot.indicators.registry import IndicatorRegistry


class IndicatorEngine:
    def __init__(
        self,
        registry: IndicatorRegistry,
    ) -> None:
        self._registry = registry

    def process(
        self,
        candle: Candle,
    ) -> None:
        for indicator in self._registry:
            indicator.update(candle)

    def handle_candle_completed(
        self,
        event: CandleCompletedEvent,
    ) -> None:
        self.process(event.candle)
