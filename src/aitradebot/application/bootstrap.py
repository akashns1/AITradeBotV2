from dataclasses import dataclass

from aitradebot.analysis.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.application.events.candle_completed_event import (
    CandleCompletedEvent,
)
from aitradebot.application.events.event_bus import EventBus
from aitradebot.market.market_engine import MarketEngine
from aitradebot.trading.trade_decision_engine import (
    TradeDecisionEngine,
)
from aitradebot.trading.trading_pipeline import TradingPipeline
from aitradebot.domain.market import Candle
from aitradebot.trading.trade_decision_engine import (
    TradeDecision,
    TradeDecisionEngine,
)

@dataclass
class Application:
    event_bus: EventBus
    market_engine: MarketEngine
    trading_pipeline: TradingPipeline


def create_application() -> Application:
    event_bus = EventBus()

    market_engine = MarketEngine(event_bus)

    pipeline = TradingPipeline(
        event_bus=event_bus,
        swing_detector=SwingDetector(),
        market_structure_analyzer=MarketStructureAnalyzer(),
        trade_decision_engine=TradeDecisionEngine(),
    )

    event_bus.subscribe(
        CandleCompletedEvent,
        pipeline.handle_candle_completed,
    )

    return Application(
        event_bus=event_bus,
        market_engine=market_engine,
        trading_pipeline=pipeline,
    )
