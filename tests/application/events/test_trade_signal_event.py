from dataclasses import is_dataclass
from datetime import datetime, date

from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.application.events import TradeSignalEvent
from aitradebot.domain.common import Instrument
from aitradebot.domain.option import (
    OptionContract,
    OptionType,
)
from aitradebot.domain.trading import TradingInstrument


def test_creates_trade_signal_event():

    event = TradeSignalEvent(
        trading_instrument=TradingInstrument(
            instrument=Instrument(
                symbol="NIFTY",
                exchange="NSE",
            ),
            strike_interval=50,
        ),
        option_contract=OptionContract(
            symbol="NIFTY",
            strike=25150,
            option_type=OptionType.CALL,
            expiry=date(2026, 8, 6),
        ),
        direction=MarketDirection.BULLISH,
        entry_price=214.50,
        timestamp=datetime(2026, 8, 3, 9, 32),
    )

    assert is_dataclass(event)
    assert event.entry_price == 214.50
    assert event.direction == MarketDirection.BULLISH