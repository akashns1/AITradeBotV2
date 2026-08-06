from datetime import date

from aitradebot.domain.option import (
    OptionContract,
    OptionType,
    OptionWatchlist,
)


def test_creates_option_watchlist():
    watchlist = OptionWatchlist(
        call=OptionContract(
            symbol="NIFTY",
            strike=25150,
            option_type=OptionType.CALL,
            expiry=date(2026, 8, 6),
        ),
        put=OptionContract(
            symbol="NIFTY",
            strike=25200,
            option_type=OptionType.PUT,
            expiry=date(2026, 8, 6),
        ),
    )

    assert watchlist.call.strike == 25150
    assert watchlist.put.strike == 25200
