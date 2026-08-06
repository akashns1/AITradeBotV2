"""
instrument.py

Represents a resolved tradable instrument.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BrokerInstrument:

    security_id: str

    market_feed_segment: int

    rest_segment: str

    instrument_type: str

    symbol: str