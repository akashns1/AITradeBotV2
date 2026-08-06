from aitradebot.analysis.market_direction import MarketDirection


def test_market_direction_values():
    assert MarketDirection.BULLISH.value == "BULLISH"
    assert MarketDirection.BEARISH.value == "BEARISH"
    assert MarketDirection.NEUTRAL.value == "NEUTRAL"