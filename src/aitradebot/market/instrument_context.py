from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle, Tick
from aitradebot.market.candle_builder import CandleBuilder


class InstrumentContext:
    def __init__(
        self,
        instrument: Instrument,
        timeframe: TimeFrame,
    ) -> None:
        self._instrument = instrument
        self._timeframe = timeframe

        self._candle_builder = CandleBuilder(
            instrument=instrument,
            timeframe=timeframe,
        )

        self._last_tick: Tick | None = None
        self._last_candle: Candle | None = None

    def process_tick(
        self,
        tick: Tick,
    ) -> list[Candle]:
        self._last_tick = tick

        candles = self._candle_builder.process(tick)

        if candles:
            self._last_candle = candles[-1]

        return candles
