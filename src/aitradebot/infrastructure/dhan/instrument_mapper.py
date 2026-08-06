"""
Broker Instrument Mapper
"""

from aitradebot.domain.common import Instrument
from aitradebot.infrastructure.dhan.instrument import BrokerInstrument


class InstrumentMapper:
    """
    Converts BrokerInstrument into a domain Instrument.
    """

    def map(
        self,
        broker_instrument: BrokerInstrument,
    ) -> Instrument:

        return Instrument(
            symbol=broker_instrument.symbol,
            exchange=broker_instrument.rest_segment,
        )