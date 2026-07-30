from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.indicators.ema import EMA


def create_candle(close: float) -> Candle:
    return Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=close,
        high=close,
        low=close,
        close=close,
        volume=100,
        start_time=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 2, tzinfo=UTC),
    )


def test_ema_can_be_created() -> None:
    ema = EMA(period=20)

    assert ema is not None


def test_ema_starts_with_no_value() -> None:
    ema = EMA(period=20)

    assert ema.value is None


def test_ema_stores_period() -> None:
    ema = EMA(period=20)

    assert ema.period == 20


def test_ema_updates_using_recursive_formula() -> None:
    ema = EMA(period=3)

    ema.update(create_candle(10))
    ema.update(create_candle(20))
    ema.update(create_candle(30))

    # Initial EMA = SMA = 20
    assert ema.value == 20

    ema.update(create_candle(40))

    # Multiplier = 2 / (3 + 1) = 0.5
    #
    # EMA = (40 × 0.5) + (20 × 0.5)
    #     = 30
    assert ema.value == 30
