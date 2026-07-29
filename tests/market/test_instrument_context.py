from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.market.instrument_context import InstrumentContext


def test_instrument_context_can_be_created() -> None:
    context = InstrumentContext(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
    )

    assert context is not None
