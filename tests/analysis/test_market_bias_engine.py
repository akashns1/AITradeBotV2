from aitradebot.analysis.market_bias_engine import MarketBiasEngine
from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.analysis.market_structure_analyzer import (
    MarketStructure,
)


def test_returns_bullish_bias():
    engine = MarketBiasEngine()

    bias = engine.analyze(
        MarketStructure(
            is_higher_high=True,
            is_higher_low=True,
            is_lower_high=False,
            is_lower_low=False,
            is_bullish_bos=True,
            is_bearish_bos=False,
        )
    )

    assert bias.direction == MarketDirection.BULLISH


def test_returns_bearish_bias():
    engine = MarketBiasEngine()

    bias = engine.analyze(
        MarketStructure(
            is_higher_high=False,
            is_higher_low=False,
            is_lower_high=True,
            is_lower_low=True,
            is_bullish_bos=False,
            is_bearish_bos=True,
        )
    )

    assert bias.direction == MarketDirection.BEARISH


def test_returns_neutral_bias():
    engine = MarketBiasEngine()

    bias = engine.analyze(
        MarketStructure(
            is_higher_high=False,
            is_higher_low=False,
            is_lower_high=False,
            is_lower_low=False,
            is_bullish_bos=False,
            is_bearish_bos=False,
        )
    )

    assert bias.direction == MarketDirection.NEUTRAL