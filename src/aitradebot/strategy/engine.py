from aitradebot.signals import Signal
from aitradebot.strategy.base_strategy import BaseStrategy
from aitradebot.strategy.market_context import MarketContext


class StrategyEngine:
    def __init__(
        self,
        strategies: list[BaseStrategy],
    ) -> None:
        self._strategies = strategies

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Signal]:
        signals: list[Signal] = []

        for strategy in self._strategies:
            signal = strategy.evaluate(context)

            if signal is not None:
                signals.append(signal)

        return signals
