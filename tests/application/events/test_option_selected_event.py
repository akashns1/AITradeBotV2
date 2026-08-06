from datetime import date

from aitradebot.application.events import OptionSelectedEvent
from aitradebot.domain.option import (
    OptionContract,
    OptionType,
)


def test_creates_option_selected_event():
    event = OptionSelectedEvent(
        contract=OptionContract(
            symbol="NIFTY",
            strike=25000,
            option_type=OptionType.CALL,
            expiry=date(2026, 8, 6),
        )
    )

    assert event.contract.symbol == "NIFTY"
    assert event.contract.option_type == OptionType.CALL