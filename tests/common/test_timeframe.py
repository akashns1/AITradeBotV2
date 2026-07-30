from aitradebot.domain.common import TimeFrame


def test_timeframe_values() -> None:
    assert TimeFrame.TWO_MINUTES.value == "2m"
    assert TimeFrame.FIFTEEN_MINUTES.value == "15m"


def test_timeframe_minutes() -> None:
    assert TimeFrame.ONE_MINUTE.minutes == 1
    assert TimeFrame.TWO_MINUTES.minutes == 2
    assert TimeFrame.FIVE_MINUTES.minutes == 5
    