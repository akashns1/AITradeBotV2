from datetime import UTC, datetime

from aitradebot.analysis.swing_detector import SwingDetector
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.testing.builders import make_candle

def candle(high: float) -> Candle:
    return Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=high,
        low=99,
        close=101,
        volume=1000,
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
    )


def test_detects_swing_high():
    candles = [
        candle(101),
        candle(104),
        candle(108),
        candle(103),
        candle(100),
    ]

    detector = SwingDetector()

    analysis = detector.analyze(candles)

    assert len(analysis.swing_highs) == 1
    assert analysis.swing_highs[0].index == 2
    assert analysis.swing_highs[0].price == 108 

def test_detects_swing_low():
    candles = [
        make_candle(low=100),
        make_candle(low=98),
        make_candle(low=95),
        make_candle(low=99),
        make_candle(low=101),
    ]

    detector = SwingDetector()

    analysis = detector.analyze(candles)

    assert len(analysis.swing_lows) == 1

    assert analysis.swing_lows[0].index == 2
    assert analysis.swing_lows[0].price == 95