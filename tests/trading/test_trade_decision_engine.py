from aitradebot.analysis.market_structure_analyzer import MarketStructure
from aitradebot.trading.trade_decision_engine import TradeDecisionEngine


def test_returns_buy_for_bullish_bos():
    structure = MarketStructure(
        is_higher_high=True,
        is_higher_low=True,
        is_lower_high=False,
        is_lower_low=False,
        is_bullish_bos=True,
        is_bearish_bos=False,
    )

    decision = TradeDecisionEngine().decide(structure)

    assert decision.action == "BUY"
    assert decision.side == "LONG"
def test_returns_sell_for_bearish_bos():
    structure = MarketStructure(
        is_higher_high=False,
        is_higher_low=False,
        is_lower_high=True,
        is_lower_low=True,
        is_bullish_bos=False,
        is_bearish_bos=True,
    )

    decision = TradeDecisionEngine().decide(structure)

    assert decision.action == "SELL"
    assert decision.side == "SHORT"


def test_returns_none_when_no_bos():
    structure = MarketStructure(
        is_higher_high=False,
        is_higher_low=False,
        is_lower_high=False,
        is_lower_low=False,
        is_bullish_bos=False,
        is_bearish_bos=False,
    )

    decision = TradeDecisionEngine().decide(structure)

    assert decision.action == "NONE"
    assert decision.side == "NONE"