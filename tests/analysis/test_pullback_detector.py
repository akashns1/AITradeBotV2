from datetime import datetime

from aitradebot.analysis.pullback_detector import PullbackDetector
from aitradebot.analysis.trend import Trend
from aitradebot.domain.market.candle import Candle
from aitradebot.domain.common import Instrument, TimeFrame


def test_detects_pullback_in_uptrend():
    instrument = Instrument("NIFTY", "NSE")
    timeframe = TimeFrame.TWO_MINUTES

    candles = [
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=100,
            high=106,
            low=99,
            close=105,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=105,
            high=111,
            low=104,
            close=110,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=110,
            high=111,
            low=106,
            close=107,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
    ]

    detector = PullbackDetector()

    analysis = detector.analyze(candles, Trend.UP)

    assert analysis.detected is True

def test_no_pullback_when_last_candle_is_bullish_in_uptrend():
    instrument = Instrument("NIFTY", "NSE")
    timeframe = TimeFrame.TWO_MINUTES

    candles = [
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=100,
            high=106,
            low=99,
            close=105,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=105,
            high=111,
            low=104,
            close=110,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=110,
            high=114,
            low=109,
            close=113,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
    ]

    detector = PullbackDetector()

    analysis = detector.analyze(candles, Trend.UP)

    assert analysis.detected is False
def test_detects_pullback_in_downtrend():
    instrument = Instrument("NIFTY", "NSE")
    timeframe = TimeFrame.TWO_MINUTES

    candles = [
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=110,
            high=111,
            low=105,
            close=106,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=106,
            high=107,
            low=100,
            close=101,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=101,
            high=105,
            low=100,
            close=104,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
    ]

    detector = PullbackDetector()

    analysis = detector.analyze(candles, Trend.DOWN)

    assert analysis.detected is True
