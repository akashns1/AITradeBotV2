from aitradebot.strategy.base_strategy import BaseStrategy


class StrategyEngine:
    def __init__(
        self,
        strategies: list[BaseStrategy],
    ) -> None:
        self._strategies = strategies
