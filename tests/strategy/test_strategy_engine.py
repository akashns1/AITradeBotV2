from aitradebot.strategy.engine import StrategyEngine

from aitradebot.strategy.base_strategy import BaseStrategy


class DummyStrategy(BaseStrategy):
    def evaluate(self, candle):
        return None


def test_strategy_engine_can_be_created() -> None:
    strategy = DummyStrategy()

    engine = StrategyEngine([strategy])

    assert engine is not None
