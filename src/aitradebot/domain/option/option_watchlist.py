from dataclasses import dataclass

from aitradebot.domain.option import OptionContract


@dataclass(frozen=True, slots=True)
class OptionWatchlist:
    call: OptionContract
    put: OptionContract