from aitradebot.indicators import BaseIndicator
from aitradebot.indicators.registry import IndicatorRegistry


def test_registry_starts_empty() -> None:
    registry = IndicatorRegistry()

    assert len(registry) == 0


class DummyIndicator(BaseIndicator):
    def update(self, candle) -> None:
        pass

    @property
    def value(self) -> float | None:
        return None


def test_registry_can_register_indicator() -> None:
    registry = IndicatorRegistry()

    indicator = DummyIndicator()

    registry.register(indicator)

    assert len(registry) == 1
