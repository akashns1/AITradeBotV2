from datetime import date

from aitradebot.analysis.market_bias import MarketBias
from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.domain.option import (
    OptionContract,
    OptionType,
)
from aitradebot.domain.trading import TradingInstrument
from aitradebot.trading.strike_selector import StrikeSelector


class OptionSelector:
    def __init__(
        self,
        strike_selector: StrikeSelector,
    ):
        self._strike_selector = strike_selector

    def select(
        self,
        trading_instrument: TradingInstrument,
        spot_price: float,
        bias: MarketBias,
        expiry: date,
    ) -> OptionContract:

        strike = self._strike_selector.select(
            trading_instrument=trading_instrument,
            spot_price=spot_price,
            direction=bias.direction,
        )

        option_type = (
            OptionType.CALL
            if bias.direction == MarketDirection.BULLISH
            else OptionType.PUT
        )

        return OptionContract(
            symbol=trading_instrument.instrument.symbol,
            strike=strike,
            option_type=option_type,
            expiry=expiry,
        )