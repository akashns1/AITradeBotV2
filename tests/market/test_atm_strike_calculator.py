from aitradebot.market.atm_strike_calculator import (
    ATMStrikeCalculator,
)


def test_calculates_atm():

    calculator = ATMStrikeCalculator()

    assert (
        calculator.calculate(
            spot_price=24383,
            strike_step=50,
        )
        == 24400
    )


def test_rounds_down():

    calculator = ATMStrikeCalculator()

    assert (
        calculator.calculate(
            spot_price=24324,
            strike_step=50,
        )
        == 24300
    )


def test_exact_strike():

    calculator = ATMStrikeCalculator()

    assert (
        calculator.calculate(
            spot_price=24350,
            strike_step=50,
        )
        == 24350
    )