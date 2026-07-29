from aitradebot.domain.common import Instrument


def test_full_symbol() -> None:
    instrument = Instrument(
        symbol="NIFTY",
        exchange="NSE",
    )

    assert instrument.full_symbol == "NSE:NIFTY"
