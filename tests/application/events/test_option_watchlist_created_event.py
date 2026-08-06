from datetime import date

from aitradebot.application.events import (
    OptionWatchlistCreatedEvent,
)
from aitradebot.domain.option import (
    OptionContract,
    OptionType,
    OptionWatchlist,
)


def test_creates_option_watchlist_event():
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

    event = OptionWatchlistCreatedEvent(
        watchlist=watchlist,
    )

    assert event.watchlist == watchlist