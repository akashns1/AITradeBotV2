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
from aitradebot.trading.stop_loss_calculator import (
    StopLossCalculator,
)

class TradingPipeline:
    def __init__(
        self,
        event_bus: EventBus,
        swing_detector: SwingDetector,
        market_structure_analyzer: MarketStructureAnalyzer,
        trade_decision_engine: TradeDecisionEngine,
        stop_loss_calculator: StopLossCalculator,
    ):
        self._event_bus = event_bus
        self._candles: list[Candle] = []

        self._swing_detector = swing_detector
        self._market_structure_analyzer = market_structure_analyzer
        self._trade_decision_engine = trade_decision_engine
        self._stop_loss_calculator = stop_loss_calculator


    def handle_candle_completed(
        self,
        event: CandleCompletedEvent,
    ) -> None:

        print("\n========== TRADING PIPELINE ==========")

        print("New Candle")
        print(event.candle)

        self._candles.append(event.candle)

        print(f"Candle Count : {len(self._candles)}")

        decision = self.process(
            self._candles,
        )

        print("Trade Decision")
        print(decision)

        if decision.side == "NONE":

            print("No trade.\n")

            return

        stop_loss = self._stop_loss_calculator.calculate(
            decision,
            event.candle,
        )

        print(f"Stop Loss : {stop_loss}")

        self._event_bus.publish(
            TradeDecisionEvent(
                decision=decision,
                candle=event.candle,
                stop_loss=stop_loss,
            )
        )

        print("TradeDecisionEvent Published")
        print("=====================================\n")

    def process(
        self,
        candles: list[Candle],
    ) -> TradeDecision:

        swing_analysis = self._swing_detector.analyze(
            candles,
        )

        print("\nSwing Analysis")
        print(swing_analysis)

        market_structure = (
            self._market_structure_analyzer.analyze(
                swing_analysis,
            )
        )

        print("\nMarket Structure")
        print(market_structure)

        decision = (
            self._trade_decision_engine.decide(
                market_structure,
            )
        )

        print("\nDecision")
        print(decision)

        return decision