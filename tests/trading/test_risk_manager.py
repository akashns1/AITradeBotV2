from datetime import datetime, timedelta, timezone

from aitradebot.trading.risk_manager import RiskManager
from aitradebot.trading.trade import Trade


def create_trade(
    profit_loss: float,
) -> Trade:

    return Trade(
        side="LONG",
        entry_price=100.0,
        exit_price=110.0,
        profit_loss=profit_loss,
    )


def test_can_trade_initially() -> None:

    manager = RiskManager(
        daily_target_points=25,
        daily_stop_loss_points=10,
        cooldown_minutes=20,
    )

    now = datetime.now(timezone.utc)

    assert manager.can_trade(now)


def test_daily_target_blocks_trading() -> None:

    manager = RiskManager(
        daily_target_points=25,
        daily_stop_loss_points=10,
        cooldown_minutes=20,
    )

    now = datetime.now(timezone.utc)

    manager.record_trade(
        create_trade(25),
        now,
    )

    future = now + timedelta(minutes=21)

    assert not manager.can_trade(future)


def test_daily_stop_loss_blocks_trading() -> None:

    manager = RiskManager(
        daily_target_points=25,
        daily_stop_loss_points=10,
        cooldown_minutes=20,
    )

    now = datetime.now(timezone.utc)

    manager.record_trade(
        create_trade(-10),
        now,
    )

    future = now + timedelta(minutes=21)

    assert not manager.can_trade(future)


def test_cooldown_blocks_trading() -> None:

    manager = RiskManager(
        daily_target_points=25,
        daily_stop_loss_points=10,
        cooldown_minutes=20,
    )

    now = datetime.now(timezone.utc)

    manager.record_trade(
        create_trade(5),
        now,
    )

    assert not manager.can_trade(
        now + timedelta(minutes=10),
    )

    assert manager.can_trade(
        now + timedelta(minutes=21),
    )