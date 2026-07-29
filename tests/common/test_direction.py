from aitradebot.domain.common import Direction


def test_direction_values() -> None:
    assert Direction.BUY.value == "BUY"
    assert Direction.SELL.value == "SELL"
