"""
Strike Selector
"""


class StrikeSelector:
    """
    Calculates the option strike to trade.
    """

    def select(
        self,
        atm: int,
        signal: str,
        option_style: str,
        strike_step: int,
        itm_strikes: int = 0,
    ) -> int:

        signal = signal.upper()
        option_style = option_style.upper()

        offset = itm_strikes * strike_step

        if option_style == "ATM":
            return atm

        if signal == "BULLISH":

            if option_style == "ITM":
                return atm - offset

            if option_style == "OTM":
                return atm + offset

        if signal == "BEARISH":

            if option_style == "ITM":
                return atm + offset

            if option_style == "OTM":
                return atm - offset

        raise ValueError(
            f"Unsupported configuration "
            f"(signal={signal}, "
            f"option_style={option_style})"
        )