from datetime import datetime, timedelta

from aitradebot.trading import CooldownManager


def test_is_ready_when_no_trade_has_occurred():
    manager = CooldownManager(
        cooldown=timedelta(minutes=20),
    )

    assert manager.is_ready(
        datetime(2026, 8, 3, 9, 30),
    )


def test_not_ready_during_cooldown():
    manager = CooldownManager(
        cooldown=timedelta(minutes=20),
    )

    manager.trade_closed(
        datetime(2026, 8, 3, 9, 30),
    )

    assert not manager.is_ready(
        datetime(2026, 8, 3, 9, 45),
    )


def test_ready_after_cooldown():
    manager = CooldownManager(
        cooldown=timedelta(minutes=20),
    )

    manager.trade_closed(
        datetime(2026, 8, 3, 9, 30),
    )

    assert manager.is_ready(
        datetime(2026, 8, 3, 9, 50),
    )


def test_ready_after_longer_than_cooldown():
    manager = CooldownManager(
        cooldown=timedelta(minutes=20),
    )

    manager.trade_closed(
        datetime(2026, 8, 3, 9, 30),
    )

    assert manager.is_ready(
        datetime(2026, 8, 3, 10, 15),
    )