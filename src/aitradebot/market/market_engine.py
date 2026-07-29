from aitradebot.application.events import CandleCompletedEvent
from aitradebot.application.events.event_bus import EventBus
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle, Tick
from aitradebot.market.instrument_context import InstrumentContext


class MarketEngine:
    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:
        self._event_bus = event_bus
        self._contexts: dict[Instrument, InstrumentContext] = {}

    def add_instrument(
        self,
        instrument: Instrument,
        timeframe: TimeFrame,
    ) -> None:
        self._contexts[instrument] = InstrumentContext(
            instrument=instrument,
            timeframe=timeframe,
        )

    def process_tick(
        self,
        tick: Tick,
    ) -> list[Candle]:
        context = self._contexts[tick.instrument]

        candles = context.process_tick(tick)

        for candle in candles:
            self._event_bus.publish(
                CandleCompletedEvent(
                    candle=candle,
                )
            )

        return candles
