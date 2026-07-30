from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.signals.signal import Signal
from aitradebot.signals.signal_type import SignalType


def test_signal_can_be_created() -> None:
    signal = Signal(
        signal_type=SignalType.BUY,
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        timestamp=datetime(2026, 1, 1, 9, 16, tzinfo=UTC),
    )

    assert signal.signal_type == SignalType.BUY
