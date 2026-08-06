from aitradebot.analysis.market_bias_engine import MarketBiasEngine
from aitradebot.analysis.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.application.events import (
    CandleCompletedEvent,
    MarketBiasEvent,
)
from aitradebot.application.events.event_bus import EventBus
from aitradebot.domain.trading import TradingInstrument


class MarketBiasPipeline:
    def __init__(
        self,
        event_bus: EventBus,
        swing_detector: SwingDetector,
        market_structure_analyzer: MarketStructureAnalyzer,
        market_bias_engine: MarketBiasEngine,
        trading_instrument: TradingInstrument,
        
    ):
        self._event_bus = event_bus
        self._candles = []

        self._swing_detector = swing_detector
        self._market_structure_analyzer = market_structure_analyzer
        self._market_bias_engine = market_bias_engine
        self._trading_instrument = trading_instrument
    def handle_candle_completed(
        self,
        event: CandleCompletedEvent,
    ) -> None:
        self._candles.append(event.candle)

        bias = self.process(self._candles)

        self._event_bus.publish(
            MarketBiasEvent(
                bias=bias,
                spot_price=event.candle.close,
                trading_instrument=self._trading_instrument,
            )
        )

    def process(self, candles):
        swing_analysis = self._swing_detector.analyze(candles)

        market_structure = self._market_structure_analyzer.analyze(
            swing_analysis,
        )

        return self._market_bias_engine.analyze(
            market_structure,
        )