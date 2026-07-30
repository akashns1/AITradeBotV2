from aitradebot.signals.signal_type import SignalType


def test_signal_type_contains_buy_sell_hold() -> None:
    assert SignalType.BUY.value == "BUY"
    assert SignalType.SELL.value == "SELL"
    assert SignalType.HOLD.value == "HOLD"
