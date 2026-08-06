from datetime import UTC, datetime

import pytest

from aitradebot.domain.common.instrument import Instrument
from aitradebot.domain.common.timeframe import TimeFrame
from aitradebot.domain.market import Candle


@pytest.fixture
def create_candle():
    def _create(close: float) -> Candle:
        return Candle(
            instrument=Instrument("NIFTY", "NSE"),
            timeframe=TimeFrame.TWO_MINUTES,
            open=close,
            high=close,
            low=close,
            close=close,
            volume=100,
            start_time=datetime(2026, 1, 1, 9, 15, tzinfo=UTC),
            end_time=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
        )

    return _create