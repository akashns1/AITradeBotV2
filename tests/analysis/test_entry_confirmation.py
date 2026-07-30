from datetime import datetime

from aitradebot.analysis.entry_confirmation import EntryConfirmation
from aitradebot.analysis.trend import Trend
#from aitradebot.domain.market import Candle, Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.domain.common.instrument import Instrument
from aitradebot.domain.common.timeframe import TimeFrame

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

    analysis = confirmation.analyze(candles, Trend.UP)

    assert analysis.confirmed is True