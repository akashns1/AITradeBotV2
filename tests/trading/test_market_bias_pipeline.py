from aitradebot.analysis.market_bias import MarketBias
from aitradebot.analysis.market_bias_engine import MarketBiasEngine
from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.analysis.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.application.events.event_bus import EventBus
from aitradebot.domain.common import Instrument
from aitradebot.domain.trading import TradingInstrument
from aitradebot.trading.market_bias_pipeline import MarketBiasPipeline


def test_process_returns_market_bias(create_candle):
    candles = [
        create_candle(100),
        create_candle(105),
        create_candle(101),
        create_candle(110),
        create_candle(106),
    ]

    event_bus = EventBus()

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    pipeline = MarketBiasPipeline(
        event_bus=event_bus,
        swing_detector=SwingDetector(),
        market_structure_analyzer=MarketStructureAnalyzer(),
        market_bias_engine=MarketBiasEngine(),
        trading_instrument=trading_instrument,
    )

    bias = pipeline.process(candles)

    assert isinstance(bias, MarketBias)
    assert bias.direction in (
        MarketDirection.BULLISH,
        MarketDirection.BEARISH,
        MarketDirection.NEUTRAL,
    )