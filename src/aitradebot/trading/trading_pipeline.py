from aitradebot.application.events.candle_completed_event import (
    CandleCompletedEvent,
)
from aitradebot.analysis.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.trading.trade_decision_engine import TradeDecisionEngine

class TradingPipeline:
    def __init__(
        self,
        swing_detector: SwingDetector,
        market_structure_analyzer: MarketStructureAnalyzer,
        trade_decision_engine: TradeDecisionEngine,
    ):
        
        self._candles = []
        self._swing_detector = swing_detector
        self._market_structure_analyzer = market_structure_analyzer
        self._trade_decision_engine = trade_decision_engine

    def handle_candle_completed(
        self,
        event: CandleCompletedEvent,
    ) -> None:
        self._candles.append(event.candle)

        decision = self.process(self._candles)

        print(
            f"{event.candle.end_time:%H:%M} | "
            f"Decision={decision.action}"
        )
        
    def process(self, candles):
        swing_analysis = self._swing_detector.analyze(candles)

        market_structure = self._market_structure_analyzer.analyze(
            swing_analysis
        )

        return self._trade_decision_engine.decide(
            market_structure
        )   