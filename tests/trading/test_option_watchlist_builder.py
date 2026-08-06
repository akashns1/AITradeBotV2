from datetime import date

from aitradebot.domain.common import Instrument
from aitradebot.domain.option import OptionType
from aitradebot.domain.trading import TradingInstrument
from aitradebot.trading.option_watchlist_builder import (
    OptionWatchlistBuilder,
)
from aitradebot.trading.strike_selector import StrikeSelector


def test_builds_itm_watchlist():
    builder = OptionWatchlistBuilder(
        strike_selector=StrikeSelector(),
    )

    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    watchlist = builder.build(
        trading_instrument=trading_instrument,
        spot_price=25172,
        expiry=date(2026, 8, 6),
    )

    assert watchlist.call.option_type == OptionType.CALL
    assert watchlist.call.strike == 25150

    assert watchlist.put.option_type == OptionType.PUT
    assert watchlist.put.strike == 25200