"""
ATM Strike Calculator
"""

import math


class ATMStrikeCalculator:
    """
    Calculates the ATM strike for an underlying.
    """

    def calculate(
        self,
        spot_price: float,
        strike_step: int,
    ) -> int:
        """
        Example:

        Spot : 24383
        Step : 50

        ATM  : 24400
        """

        return (
            math.floor(
                (spot_price + strike_step / 2)
                / strike_step
            )
            * strike_step
        )