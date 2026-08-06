from aitradebot.application.events import CandleCompletedEvent
from aitradebot.application.events.event_bus import EventBus
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle, Tick
from aitradebot.market.instrument_context import InstrumentContext
from aitradebot.infrastructure.logging.market_logger import (
    logger,
)

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
        print("\n========== MARKET ENGINE ==========")

        print("Registered instruments:")
        for inst in self._contexts:
            print(inst)

        print("\nIncoming instrument:")
        print(tick.instrument)

        print("===================================")
        logger.info(
            "Tick | %s | %s | %.2f",
            tick.instrument.symbol,
            tick.timestamp,
            tick.price,
        )
        context = self._contexts[tick.instrument]

        candles = context.process_tick(tick)

        logger.info(
            "Completed candles: %s",
            len(candles),
        )

        for candle in candles:
            logger.info(
                "Candle completed: %s",
                candle,
            )

            self._event_bus.publish(
                CandleCompletedEvent(
                    candle=candle,
                )
            )

        return candles