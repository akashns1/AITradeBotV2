from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.domain.trading import TradingInstrument


class StrikeSelector:
    
    def select(
        self,
        trading_instrument: TradingInstrument,
        spot_price: float,
        direction: MarketDirection,
    ) -> int:

        interval = trading_instrument.strike_interval

        lower_strike = int(spot_price // interval) * interval
        upper_strike = lower_strike + interval

        if direction == MarketDirection.BULLISH:
            return lower_strike

        if direction == MarketDirection.BEARISH:
            return upper_strike

        raise ValueError(
            f"Unsupported direction: {direction}"
        )