from aitradebot.trading.exit_reason import ExitReason
from aitradebot.trading.position import Position
from aitradebot.trading.position_manager import PositionManager
from aitradebot.trading.exit_reason import ExitReason

def test_returns_stop_loss_for_long_position():
    manager = PositionManager()

    position = Position(
        side="LONG",
        entry_price=100.0,
        stop_loss=98.0,
        target_price=104,
    )

    reason = manager.should_close(
        position,
        current_price=98.0,
    )

    assert reason == ExitReason.STOP_LOSS
def test_returns_take_profit_for_long_position():
    manager = PositionManager()

    position = Position(
        side="LONG",
        entry_price=100,
        stop_loss=98,
        target_price=104,
    )

    reason = manager.should_close(
        position,
        current_price=104,
    )

    assert reason == ExitReason.TAKE_PROFIT
def test_returns_take_profit_for_short_position():
    manager = PositionManager()

    position = Position(
        side="SHORT",
        entry_price=100,
        stop_loss=102,
        target_price=96,
    )

    reason = manager.should_close(
        position,
        current_price=96,
    )

    assert reason == ExitReason.TAKE_PROFIT
def test_returns_stop_loss_for_short_position():
    manager = PositionManager()

    position = Position(
        side="SHORT",
        entry_price=100,
        stop_loss=102,
        target_price=96,
    )

    reason = manager.should_close(
        position,
        current_price=102,
    )

    assert reason == ExitReason.STOP_LOSS