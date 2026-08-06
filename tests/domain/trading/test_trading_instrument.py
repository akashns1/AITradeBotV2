from aitradebot.domain.common import Instrument
from aitradebot.domain.trading import TradingInstrument


def test_creates_trading_instrument():
    trading_instrument = TradingInstrument(
        instrument=Instrument(
            symbol="NIFTY",
            exchange="NSE",
        ),
        strike_interval=50,
    )

    assert trading_instrument.instrument.symbol == "NIFTY"
    assert trading_instrument.instrument.exchange == "NSE"
    assert trading_instrument.strike_interval == 50