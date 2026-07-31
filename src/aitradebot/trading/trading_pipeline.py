from __future__ import annotations

from aitradebot.application.events import (
    CandleCompletedEvent,
    TradeDecisionEvent,
)
from aitradebot.application.events.event_bus import EventBus
from aitradebot.analysis.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.domain.market import Candle
from aitradebot.trading.trade_decision_engine import (
    TradeDecision,
    TradeDecisionEngine,
)


class TradingPipeline:
    def __init__(
        self,
        event_bus: EventBus,
        swing_detector: SwingDetector,
        market_structure_analyzer: MarketStructureAnalyzer,
        trade_decision_engine: TradeDecisionEngine,
    ) -> None:
        self._event_bus = event_bus
        self._candles: list[Candle] = []

        self._swing_detector = swing_detector
        self._market_structure_analyzer = market_structure_analyzer
        self._trade_decision_engine = trade_decision_engine

    def handle_candle_completed(
        self,
        event: CandleCompletedEvent,
    ) -> None:
        self._candles.append(event.candle)

        decision = self.process(self._candles)

        self._event_bus.publish(
            TradeDecisionEvent(
                decision=decision,
            )
        )

    def process(
        self,
        candles: list[Candle],
    ) -> TradeDecision:
        swing_analysis = self._swing_detector.analyze(candles)

        market_structure = self._market_structure_analyzer.analyze(
            swing_analysis
        )

        return self._trade_decision_engine.decide(
            market_structure
        )