from datetime import date

from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.domain.option import (
    OptionContract,
    OptionType,
    OptionWatchlist,
)
from aitradebot.domain.trading import TradingInstrument
from aitradebot.trading.strike_selector import StrikeSelector


class OptionWatchlistBuilder:
    def __init__(
        self,
        strike_selector: StrikeSelector,
    ):
        self._strike_selector = strike_selector

    def build(
        self,
        trading_instrument: TradingInstrument,
        spot_price: float,
        expiry: date,
    ) -> OptionWatchlist:

        call_strike = self._strike_selector.select(
            trading_instrument=trading_instrument,
            spot_price=spot_price,
            direction=MarketDirection.BULLISH,
        )

        put_strike = self._strike_selector.select(
            trading_instrument=trading_instrument,
            spot_price=spot_price,
            direction=MarketDirection.BEARISH,
        )

        return OptionWatchlist(
            call=OptionContract(
                symbol=trading_instrument.instrument.symbol,
                strike=call_strike,
                option_type=OptionType.CALL,
                expiry=expiry,
            ),
            put=OptionContract(
                symbol=trading_instrument.instrument.symbol,
                strike=put_strike,
                option_type=OptionType.PUT,
                expiry=expiry,
            ),
        )