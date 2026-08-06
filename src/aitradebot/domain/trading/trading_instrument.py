from dataclasses import dataclass

from aitradebot.domain.common import Instrument


@dataclass(frozen=True, slots=True)
class TradingInstrument:
    instrument: Instrument
    strike_interval: int