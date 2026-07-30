from aitradebot.signals.signal_generator import TradingSignal
from aitradebot.trading.paper_trade_engine import PaperTradeEngine


def test_opens_long_position_on_buy_signal():
    engine = PaperTradeEngine()

    signal = TradingSignal(action="BUY")

    engine.process(
        signal,
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
    )

    assert engine.position is not None
    assert engine.position.side == "LONG"
    assert engine.position.entry_price == 100.0
    assert engine.position.stop_loss == 98.0

def test_opens_short_position_on_sell_signal():
    engine = PaperTradeEngine()

    signal = TradingSignal(action="SELL")

    engine.process(
        signal,
        current_price=100.0,
        stop_loss=102.0,
        risk_reward=2.0,
    )

    assert engine.position.stop_loss == 102.0

    assert engine.position is not None
    assert engine.position.side == "SHORT"
    assert engine.position.entry_price == 100.0

def test_wait_signal_does_not_open_position():
    engine = PaperTradeEngine()

    signal = TradingSignal(action="WAIT")

    engine.process(
        signal,
        current_price=100.0,
        stop_loss=98.0,
    )

    assert engine.has_open_position is False

def test_does_not_open_second_position():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="BUY"),
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
    )

    engine.process(
        TradingSignal(action="BUY"),
        current_price=101.0,
        stop_loss=98.0,
    )

    assert engine.position is not None
    assert engine.position.side == "LONG"
    assert engine.position.entry_price == 100.0
def test_engine_starts_with_empty_trade_history():
    engine = PaperTradeEngine()

    assert engine.trade_history == []
def test_closing_position_clears_open_position():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="BUY"),
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
    )

    engine.close_position(exit_price=105.0)

    assert engine.position is None
    assert len(engine.trade_history) == 1

    trade = engine.trade_history[0]

    assert trade.side == "LONG"
    assert trade.entry_price == 100.0
    assert trade.exit_price == 105.0
    assert trade.profit_loss == 5.0
def test_short_position_profit_loss():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="SELL"),
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
    )

    engine.close_position(exit_price=95.0)

    assert len(engine.trade_history) == 1

    trade = engine.trade_history[0]

    assert trade.side == "SHORT"
    assert trade.entry_price == 100.0
    assert trade.exit_price == 95.0
    assert trade.profit_loss == 5.0
def test_long_position_closes_when_stop_loss_is_hit():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="BUY"),
        current_price=100.0,
        stop_loss=98.0,
    )

    engine.on_price_update(99.0)

    assert engine.has_open_position is True

    engine.on_price_update(98.0)

    assert engine.has_open_position is False
    assert len(engine.trade_history) == 1

    trade = engine.trade_history[0]

    assert trade.exit_price == 98.0
    assert trade.profit_loss == -2.0
def test_long_position_closes_when_stop_loss_is_hit():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="BUY"),
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
    )

    # Stop loss not hit yet
    engine.on_price_update(99.0)

    assert engine.has_open_position is True
    assert len(engine.trade_history) == 0

    # Stop loss hit
    engine.on_price_update(98.0)

    assert engine.has_open_position is False
    assert len(engine.trade_history) == 1

    trade = engine.trade_history[0]

    assert trade.entry_price == 100.0
    assert trade.exit_price == 98.0
    assert trade.profit_loss == -2.0
def test_price_updates_after_trade_is_closed_do_nothing():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="BUY"),
        current_price=100.0,
        stop_loss=98.0,
        risk_reward=2.0,
    )

    engine.on_price_update(98.0)

    assert len(engine.trade_history) == 1

    # More price updates after the trade is closed
    engine.on_price_update(97.0)
    engine.on_price_update(96.0)
    engine.on_price_update(95.0)

    assert len(engine.trade_history) == 1
    assert engine.position is None
def test_short_position_closes_when_stop_loss_is_hit():
    engine = PaperTradeEngine()

    engine.process(
        TradingSignal(action="SELL"),
        current_price=100.0,
        stop_loss=102.0,
        risk_reward=2.0,
    )

    engine.on_price_update(101.0)

    assert engine.has_open_position is True
    assert len(engine.trade_history) == 0

    engine.on_price_update(102.0)

    assert engine.has_open_position is False
    assert len(engine.trade_history) == 1

    trade = engine.trade_history[0]

    assert trade.entry_price == 100.0
    assert trade.exit_price == 102.0
    assert trade.profit_loss == -2.0