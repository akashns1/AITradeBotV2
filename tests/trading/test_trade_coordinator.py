from datetime import datetime, timedelta

from aitradebot.trading import (
    ActiveSessionFilter,
    CooldownManager,
)
from aitradebot.trading.trade_coordinator import (
    TradeCoordinator,
)


class FakePaperTradeEngine:

    def __init__(self):
        self.position = False

    @property
    def has_open_position(self):
        return self.position


def test_can_enter_trade_when_everything_is_valid():

    engine = FakePaperTradeEngine()

    coordinator = TradeCoordinator(
        session_filter=ActiveSessionFilter(),
        cooldown_manager=CooldownManager(
            timedelta(minutes=20),
        ),
        paper_trade_engine=engine,
    )

    assert coordinator.can_enter_trade(
        datetime(2026, 8, 3, 9, 30),
    )


def test_cannot_trade_outside_session():

    engine = FakePaperTradeEngine()

    coordinator = TradeCoordinator(
        session_filter=ActiveSessionFilter(),
        cooldown_manager=CooldownManager(
            timedelta(minutes=20),
        ),
        paper_trade_engine=engine,
    )

    assert not coordinator.can_enter_trade(
        datetime(2026, 8, 3, 12, 0),
    )


def test_cannot_trade_during_cooldown():

    cooldown = CooldownManager(
        timedelta(minutes=20),
    )

    cooldown.trade_closed(
        datetime(2026, 8, 3, 9, 30),
    )

    engine = FakePaperTradeEngine()

    coordinator = TradeCoordinator(
        session_filter=ActiveSessionFilter(),
        cooldown_manager=cooldown,
        paper_trade_engine=engine,
    )

    assert not coordinator.can_enter_trade(
        datetime(2026, 8, 3, 9, 40),
    )


def test_cannot_trade_when_position_is_open():

    engine = FakePaperTradeEngine()
    engine.position = True

    coordinator = TradeCoordinator(
        session_filter=ActiveSessionFilter(),
        cooldown_manager=CooldownManager(
            timedelta(minutes=20),
        ),
        paper_trade_engine=engine,
    )

    assert not coordinator.can_enter_trade(
        datetime(2026, 8, 3, 9, 30),
    )