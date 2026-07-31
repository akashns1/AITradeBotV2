from aitradebot.trading.position_factory import PositionFactory


def test_creates_long_position():
    factory = PositionFactory()

    position = factory.create(
        side="LONG",
        entry_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
        quantity=25,
    )

    assert position.side == "LONG"
    assert position.entry_price == 100.0
    assert position.stop_loss == 98.0
    assert position.target_price == 104.0
    
def test_creates_short_position():
    factory = PositionFactory()

    position = factory.create(
        side="SHORT",
        entry_price=100.0,
        stop_loss=102.0,
        risk_reward=2.0,
        quantity=25,
    )

    assert position.side == "SHORT"
    assert position.entry_price == 100.0
    assert position.stop_loss == 102.0
    assert position.target_price == 96.0

def test_creates_position_with_quantity():
    factory = PositionFactory()

    position = factory.create(
        side="LONG",
        entry_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
        quantity=25,
    )

    assert position.quantity == 25