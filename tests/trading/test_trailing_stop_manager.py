from aitradebot.trading.position import Position
from aitradebot.trading.trailing_stop_manager import TrailingStopManager
from aitradebot.trading.trade_decision_engine import TradeDecision
from aitradebot.trading.paper_trade_engine import PaperTradeEngine


def test_moves_long_stop_loss_up():
    manager = TrailingStopManager()

    position = Position(
        side="LONG",
        entry_price=100.0,
        stop_loss=98.0,
        target_price=104.0,
        quantity=1,
    )

    updated = manager.update(
        position,
        current_price=102.0,
    )

    assert updated.stop_loss == 99.0

def test_trailing_stop_never_moves_backwards():
    manager = TrailingStopManager()

    position = Position(
        side="LONG",
        entry_price=100.0,
        stop_loss=99.0,
        target_price=104.0,
        quantity=1,
    )

    updated = manager.update(
        position,
        current_price=101.0,
    )

    assert updated.stop_loss == 99.0
def test_moves_short_stop_loss_down():
    manager = TrailingStopManager()

    position = Position(
        side="SHORT",
        entry_price=100.0,
        stop_loss=102.0,
        target_price=96.0,
        quantity=1,
    )

    updated = manager.update(
        position,
        current_price=98.0,
    )

    assert updated.stop_loss == 101.0

def test_long_position_trails_stop_loss():
    engine = PaperTradeEngine()

    engine.process(
        TradeDecision(
            action="BUY",
            side="LONG",
        ),
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
        quantity=1,
    )

    engine.on_price_update(102.0)

    assert engine.position.stop_loss == 99.0



def test_long_stop_moves_to_new_level():
    manager = TrailingStopManager()

    position = Position(
        side="LONG",
        entry_price=100,
        stop_loss=98,
        target_price=104,
        quantity=1,
    )

    updated = manager.update_to_level(
        position,
        level=101,
    )

    assert updated.stop_loss == 101
def test_update_to_level_never_moves_long_stop_backwards():
    manager = TrailingStopManager()

    position = Position(
        side="LONG",
        entry_price=100,
        stop_loss=101,
        target_price=104,
        quantity=1,
    )

    updated = manager.update_to_level(
        position,
        level=99,
    )

    assert updated.stop_loss == 101
def test_long_position_trails_stop_to_level():
    engine = PaperTradeEngine()

    engine.process(
        TradeDecision(
            action="BUY",
            side="LONG",
        ),
        current_price=100,
        stop_loss=98,
        risk_reward=2,
        quantity=1,
    )

    engine.position = engine.trailing_stop_manager.update_to_level(
        engine.position,
        level=101,
    )

    assert engine.position.stop_loss == 101
def test_on_price_update_trails_long_stop():
    engine = PaperTradeEngine()

    engine.process(
        TradeDecision(
            action="BUY",
            side="LONG",
        ),
        current_price=100,
        stop_loss=98,
        risk_reward=2,
        quantity=1,
    )

    engine.on_price_update(102)

    assert engine.position.stop_loss == 99