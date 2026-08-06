from datetime import date, datetime

from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.application.events import TradeSignalEvent
from aitradebot.domain.common import Instrument
from aitradebot.domain.option import OptionContract, OptionType
from aitradebot.domain.trading import TradingInstrument
from aitradebot.trading.trade_signal_handler import (
    TradeSignalHandler,
)


class FakeTradeCoordinator:

    def __init__(self, allowed: bool):
        self.allowed = allowed

    def can_enter_trade(self, now):
        return self.allowed


class FakePaperTradeEngine:

    def __init__(self):
        self.executed = False
        self.signal = None

    def execute(self, signal):
        self.executed = True
        self.signal = signal


def create_signal():

    return TradeSignalEvent(
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
        timestamp=datetime(2026, 8, 3, 9, 30),
    )


def test_executes_trade_when_allowed():

    engine = FakePaperTradeEngine()

    handler = TradeSignalHandler(
        trade_coordinator=FakeTradeCoordinator(True),
        paper_trade_engine=engine,
    )

    signal = create_signal()

    handler.handle(signal)

    assert engine.executed
    assert engine.signal == signal


def test_does_not_execute_when_not_allowed():

    engine = FakePaperTradeEngine()

    handler = TradeSignalHandler(
        trade_coordinator=FakeTradeCoordinator(False),
        paper_trade_engine=engine,
    )

    handler.handle(create_signal())

    assert not engine.executed