from datetime import date

from aitradebot.domain.option import (
    OptionContract,
    OptionType,
)


def test_creates_call_option_contract():
    contract = OptionContract(
        symbol="NIFTY",
        strike=25000,
        option_type=OptionType.CALL,
        expiry=date(2026, 8, 6),
    )

    assert contract.symbol == "NIFTY"
    assert contract.strike == 25000
    assert contract.option_type == OptionType.CALL
    assert contract.expiry == date(2026, 8, 6)


def test_creates_put_option_contract():
    contract = OptionContract(
        symbol="NIFTY",
        strike=25000,
        option_type=OptionType.PUT,
        expiry=date(2026, 8, 6),
    )

    assert contract.option_type == OptionType.PUT