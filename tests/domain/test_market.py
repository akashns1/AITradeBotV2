from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle


def test_bullish_candle() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=99,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.is_bullish
    assert not candle.is_bearish


def test_strong_bullish_candle() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=99,
        close=109,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.is_strong_bullish

def test_body_size() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=99,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.body_size == 8

def test_range_size() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=99,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.range_size == 11
def test_lower_wick_size() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=95,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.lower_wick_size == 5

def test_upper_wick_size() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=95,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.upper_wick_size == 2
def test_hammer_candle() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=106,
        low=90,
        close=105,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert candle.is_hammer
def test_bullish_candle_is_not_always_a_hammer() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=99,
        close=108,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )

    assert not candle.is_hammer