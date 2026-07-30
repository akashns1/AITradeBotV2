from aitradebot.trading.position import Position
from aitradebot.trading.trade_factory import TradeFactory


def test_creates_trade_for_long_position():
    factory = TradeFactory()

    position = Position(
        side="LONG",
        entry_price=100.0,
        stop_loss=98.0,
        target_price=104.0,
    )

    trade = factory.create_trade(
        position,
        exit_price=105.0,
    )

    assert trade.side == "LONG"
    assert trade.entry_price == 100.0
    assert trade.exit_price == 105.0
    assert trade.profit_loss == 5.0
def test_creates_trade_for_short_position():
    factory = TradeFactory()

    position = Position(
        side="SHORT",
        entry_price=100.0,
        stop_loss=102.0,
        target_price=104.0,
    )

    trade = factory.create_trade(
        position,
        exit_price=102.0,
    )

    assert trade.side == "SHORT"
    assert trade.entry_price == 100.0
    assert trade.exit_price == 102.0
    assert trade.profit_loss == -2.0
def test_long_profit_loss_with_quantity():
    factory = TradeFactory()

    position = Position(
        side="LONG",
        entry_price=100.0,
        stop_loss=98.0,
        target_price=104.0,
        quantity=25,
    )

    trade = factory.create_trade(position, exit_price=102.0)

    assert trade.profit_loss == 50.0
def test_short_profit_loss_with_quantity():
    factory = TradeFactory()

    position = Position(
        side="SHORT",
        entry_price=100.0,
        stop_loss=102.0,
        target_price=96.0,
        quantity=25,
    )

    trade = factory.create_trade(position, exit_price=98.0)

    assert trade.profit_loss == 50.0