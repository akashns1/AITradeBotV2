from datetime import date

from aitradebot.analysis.market_bias import MarketBias
from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.domain.common import Instrument
from aitradebot.domain.option import OptionType
from aitradebot.domain.trading import TradingInstrument
from aitradebot.trading.option_selector import OptionSelector
from aitradebot.trading.strike_selector import StrikeSelector


def test_selects_call_option():
    selector = OptionSelector(
        strike_selector=StrikeSelector(),
    )

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    option = selector.select(
        trading_instrument=trading_instrument,
        spot_price=25172,
        bias=MarketBias(
            direction=MarketDirection.BULLISH,
        ),
        expiry=date(2026, 8, 6),
    )

    assert option.symbol == "NIFTY"
    assert option.option_type == OptionType.CALL
    assert option.strike == 25150


def test_selects_put_option():
    selector = OptionSelector(
        strike_selector=StrikeSelector(),
    )

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    option = selector.select(
        trading_instrument=trading_instrument,
        spot_price=25172,
        bias=MarketBias(
            direction=MarketDirection.BEARISH,
        ),
        expiry=date(2026, 8, 6),
    )

    assert option.option_type == OptionType.PUT
    assert option.strike == 25200