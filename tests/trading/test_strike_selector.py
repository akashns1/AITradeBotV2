import pytest

from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.trading.strike_selector import StrikeSelector
from aitradebot.domain.common import Instrument
from aitradebot.domain.trading import TradingInstrument

def test_returns_itm_call_strike():
    selector = StrikeSelector()

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    strike = selector.select(
        trading_instrument=trading_instrument,
        spot_price=25172,
        direction=MarketDirection.BULLISH,
    )


def test_returns_itm_put_strike():
    selector = StrikeSelector()

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    strike = selector.select(
        trading_instrument=trading_instrument,
        spot_price=25172,
        direction=MarketDirection.BEARISH,
    )

    assert strike == 25200


def test_raises_for_neutral_direction():
    selector = StrikeSelector()

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    with pytest.raises(ValueError):
        selector.select(
            trading_instrument=trading_instrument,
            spot_price=25172,
            direction=MarketDirection.NEUTRAL,
        )