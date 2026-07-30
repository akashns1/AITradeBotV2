from aitradebot.analysis.market_structure_analyzer import MarketStructure
from aitradebot.signals.signal_generator import SignalGenerator


def test_generates_buy_signal_for_bullish_bos():
    structure = MarketStructure(
        is_higher_high=True,
        is_higher_low=True,
        is_lower_high=False,
        is_lower_low=False,
        is_bullish_bos=True,
        is_bearish_bos=False,
    )

    generator = SignalGenerator()

    signal = generator.generate(structure)

    assert signal.action == "BUY"
def test_generates_sell_signal_for_bearish_bos():
    structure = MarketStructure(
        is_higher_high=False,
        is_higher_low=False,
        is_lower_high=True,
        is_lower_low=True,
        is_bullish_bos=False,
        is_bearish_bos=True,
    )

    generator = SignalGenerator()

    signal = generator.generate(structure)

    assert signal.action == "SELL"
def test_generates_wait_signal_when_no_bos():
    structure = MarketStructure(
        is_higher_high=False,
        is_higher_low=False,
        is_lower_high=False,
        is_lower_low=False,
        is_bullish_bos=False,
        is_bearish_bos=False,
    )

    generator = SignalGenerator()

    signal = generator.generate(structure)

    assert signal.action == "WAIT"
