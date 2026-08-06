from aitradebot.analysis.market_bias import MarketBias
from aitradebot.analysis.market_direction import MarketDirection


def test_creates_bullish_market_bias():
    bias = MarketBias(
        direction=MarketDirection.BULLISH,
    )

    assert bias.direction == MarketDirection.BULLISH


def test_creates_bearish_market_bias():
    bias = MarketBias(
        direction=MarketDirection.BEARISH,
    )

    assert bias.direction == MarketDirection.BEARISH


def test_creates_neutral_market_bias():
    bias = MarketBias(
        direction=MarketDirection.NEUTRAL,
    )

    assert bias.direction == MarketDirection.NEUTRAL