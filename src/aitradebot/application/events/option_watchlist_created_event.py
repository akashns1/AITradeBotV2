from dataclasses import dataclass

from aitradebot.application.events.event import Event
from aitradebot.domain.option import OptionWatchlist


@dataclass(frozen=True, slots=True)
class OptionWatchlistCreatedEvent(Event):
    watchlist: OptionWatchlist