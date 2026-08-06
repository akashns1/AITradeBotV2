from aitradebot.market.strike_selector import StrikeSelector


def test_bullish_atm():

    selector = StrikeSelector()

    assert (
        selector.select(
            atm=24400,
            signal="BULLISH",
            option_style="ATM",
            strike_step=50,
        )
        == 24400
    )


def test_bullish_itm():

    selector = StrikeSelector()

    assert (
        selector.select(
            atm=24400,
            signal="BULLISH",
            option_style="ITM",
            strike_step=50,
            itm_strikes=1,
        )
        == 24350
    )


def test_bullish_otm():

    selector = StrikeSelector()

    assert (
        selector.select(
            atm=24400,
            signal="BULLISH",
            option_style="OTM",
            strike_step=50,
            itm_strikes=1,
        )
        == 24450
    )


def test_bearish_itm():

    selector = StrikeSelector()

    assert (
        selector.select(
            atm=24400,
            signal="BEARISH",
            option_style="ITM",
            strike_step=50,
            itm_strikes=1,
        )
        == 24450
    )


def test_bearish_otm():

    selector = StrikeSelector()

    assert (
        selector.select(
            atm=24400,
            signal="BEARISH",
            option_style="OTM",
            strike_step=50,
            itm_strikes=1,
        )
        == 24350
    )