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
from aitradebot.trading.paper_trade_engine import PaperTradeEngine
from aitradebot.trading.paper_trade_engine import PaperTradeEngine
from aitradebot.application.events.trade_decision_event import (
    TradeDecisionEvent,
)
from aitradebot.trading.stop_loss_calculator import (
    StopLossCalculator,
)

@dataclass
@dataclass
class Application:
    event_bus: EventBus
    market_engine: MarketEngine
    trading_pipeline: TradingPipeline
    paper_trade_engine: PaperTradeEngine


def create_application() -> Application:
    event_bus = EventBus()

    market_engine = MarketEngine(event_bus)
    stop_loss_calculator = StopLossCalculator()
    pipeline = TradingPipeline(
        event_bus=event_bus,
        swing_detector=SwingDetector(),
        market_structure_analyzer=MarketStructureAnalyzer(),
        trade_decision_engine=TradeDecisionEngine(),
        stop_loss_calculator=stop_loss_calculator,
    )
    paper_trade_engine = PaperTradeEngine()
    event_bus.subscribe(
        CandleCompletedEvent,
        pipeline.handle_candle_completed,
    )
    event_bus.subscribe(
        TradeDecisionEvent,
        paper_trade_engine.handle_trade_decision,
    )
    return Application(
        event_bus=event_bus,
        market_engine=market_engine,
        trading_pipeline=pipeline,
        paper_trade_engine=paper_trade_engine,
    )
