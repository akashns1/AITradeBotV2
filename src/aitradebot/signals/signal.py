from dataclasses import dataclass
from datetime import datetime

from aitradebot.domain.common import Instrument, TimeFrame

from .signal_type import SignalType


@dataclass(frozen=True, slots=True)
class Signal:
    signal_type: SignalType
    instrument: Instrument
    timeframe: TimeFrame
    timestamp: datetime
