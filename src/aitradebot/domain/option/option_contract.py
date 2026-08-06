from dataclasses import dataclass
from datetime import date

from aitradebot.domain.option.option_type import OptionType


@dataclass(frozen=True, slots=True)
class OptionContract:
    symbol: str
    strike: int
    option_type: OptionType
    expiry: date