from datetime import UTC, datetime

import pytest

from aitradebot.domain.common import Instrument
from aitradebot.domain.market import Tick


def test_tick_creation() -> None:
    tick = Tick(
        instrument=Instrument("NIFTY", "NSE"),
        price=25000.5,
        timestamp=datetime.now(UTC),
    )

    assert tick.price == 25000.5


def test_invalid_price() -> None:
    with pytest.raises(ValueError):
        Tick(
            instrument=Instrument("NIFTY", "NSE"),
            price=0,
            timestamp=datetime.now(UTC),
        )
