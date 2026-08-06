from dataclasses import dataclass

from aitradebot.application.events.event import Event
from aitradebot.domain.option import OptionContract


@dataclass(frozen=True, slots=True)
class OptionSelectedEvent(Event):
    contract: OptionContract