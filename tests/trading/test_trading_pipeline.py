from aitradebot.analysis.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.application.events.event_bus import EventBus
from aitradebot.trading.stop_loss_calculator import (
    StopLossCalculator,
)
from aitradebot.trading.trade_decision_engine import (
    TradeDecisionEngine,
)
from aitradebot.trading.trading_pipeline import TradingPipeline

def test_process_returns_trade_decision(create_candle):
    candles = [
        create_candle(100),
        create_candle(105),
        create_candle(101),
        create_candle(110),
        create_candle(106),
    ]
    event_bus = EventBus()
    pipeline = TradingPipeline(
        event_bus=event_bus,
        swing_detector=SwingDetector(),
        market_structure_analyzer=MarketStructureAnalyzer(),
        trade_decision_engine=TradeDecisionEngine(),
        stop_loss_calculator=StopLossCalculator(),
    )

    decision = pipeline.process(candles)

    assert decision is not None