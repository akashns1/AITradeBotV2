from aitradebot.application.events import CandleCompletedEvent
from aitradebot.trading.trading_pipeline import TradingPipeline


class CandleCompletedHandler:
    def __init__(self) -> None:
        self._pipeline = TradingPipeline()
        self._candles = []

    def __call__(self, event: CandleCompletedEvent) -> None:
        self._candles.append(event.candle)

        decision = self._pipeline.process(self._candles)

        print(f"Trade Decision: {decision.action}")