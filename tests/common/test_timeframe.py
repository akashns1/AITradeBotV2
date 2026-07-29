from aitradebot.domain.common import TimeFrame


def test_timeframe_values() -> None:
    assert TimeFrame.TWO_MINUTES.value == "2m"
    assert TimeFrame.FIFTEEN_MINUTES.value == "15m"
