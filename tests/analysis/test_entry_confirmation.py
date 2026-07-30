from datetime import datetime

from aitradebot.analysis.entry_confirmation import EntryConfirmation
from aitradebot.analysis.trend import Trend
#from aitradebot.domain.market import Candle, Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.domain.common.instrument import Instrument
from aitradebot.domain.common.timeframe import TimeFrame
from aitradebot.analysis.pullback_analysis import PullbackAnalysis
from datetime import UTC, datetime


def bullish_candle() -> Candle:
    return Candle(
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


def test_confirms_entry_after_pullback_in_uptrend():
    instrument = Instrument("NIFTY", "NSE")
    timeframe = TimeFrame.TWO_MINUTES

    candles = [
        # Bullish
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
        # Bullish
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
        # Pullback
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
        # Confirmation
        Candle(
            instrument=instrument,
            timeframe=timeframe,
            open=107,
            high=113,
            low=106,
            close=112,
            volume=1000,
            start_time=datetime.now(),
            end_time=datetime.now(),
        ),
    ]

    confirmation = EntryConfirmation()

    analysis = confirmation.analyze(
        candles,
        Trend.UP,
        PullbackAnalysis(detected=True),
    )

    assert analysis.confirmed is True
def test_does_not_confirm_when_no_pullback_exists():
    candles = [
        bullish_candle(),
        bullish_candle(),
        bullish_candle(),
        bullish_candle(),
    ]

    confirmation = EntryConfirmation()

    pullback = PullbackAnalysis(detected=False)

    analysis = confirmation.analyze(
        candles,
        Trend.UP,
        pullback,
    )

    assert analysis.confirmed is False

def test_does_not_confirm_on_weak_bullish_candle():
    candles = [
        bullish_candle(),
        bullish_candle(),
        bullish_candle(),
        Candle(
            instrument=Instrument("NIFTY", "NSE"),
            timeframe=TimeFrame.TWO_MINUTES,
            open=100,
            high=110,
            low=99,
            close=105,  # bullish, but weak body
            volume=1000,
            start_time=datetime.now(UTC),
            end_time=datetime.now(UTC),
        ),
    ]

    confirmation = EntryConfirmation()

    analysis = confirmation.analyze(
        candles,
        Trend.UP,
        PullbackAnalysis(detected=True),
    )

    assert analysis.confirmed is False