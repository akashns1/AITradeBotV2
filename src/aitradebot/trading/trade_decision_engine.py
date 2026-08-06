from dataclasses import dataclass

from aitradebot.analysis.market_structure_analyzer import (
    MarketStructure,
)


@dataclass(frozen=True)
class TradeDecision:
    action: str
    option_type: str


class TradeDecisionEngine:

    def decide(
        self,
        structure: MarketStructure,
    ) -> TradeDecision:

        if structure.is_bullish_bos:
            return TradeDecision(
                action="BUY",
                option_type="CALL",
            )

        if structure.is_bearish_bos:
            return TradeDecision(
                action="BUY",
                option_type="PUT",
            )

        return TradeDecision(
            action="NONE",
            option_type="NONE",
        )