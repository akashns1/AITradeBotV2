from dataclasses import dataclass

from aitradebot.application.events.event import Event
from aitradebot.domain.market import Candle


@dataclass(frozen=True, slots=True)
class CandleCompletedEvent(Event):
    candle: Candle
