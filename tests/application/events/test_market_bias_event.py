from aitradebot.analysis.market_bias import MarketBias
from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.application.events import MarketBiasEvent
from aitradebot.domain.common import Instrument
from aitradebot.domain.trading import TradingInstrument


def test_creates_market_bias_event():
    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    event = MarketBiasEvent(
        bias=MarketBias(
            direction=MarketDirection.BULLISH,
        ),
        spot_price=25172,
        trading_instrument=trading_instrument,
    )

    assert event.bias.direction == MarketDirection.BULLISH
    assert event.spot_price == 25172
    assert event.trading_instrument == trading_instrument