from aitradebot.strategy.base_strategy import BaseStrategy


def test_base_strategy_cannot_be_instantiated() -> None:
    try:
        BaseStrategy()
        assert False
    except TypeError:
        assert True
