from dataclasses import dataclass

from aitradebot.analysis.market_structure_analyzer import MarketStructure


@dataclass(frozen=True)
class TradeDecision:
    action: str
    side: str


class TradeDecisionEngine:

    def decide(self, structure: MarketStructure) -> TradeDecision:
        if structure.is_bullish_bos:
            return TradeDecision(
                action="BUY",
                side="LONG",
            )

        if structure.is_bearish_bos:
            return TradeDecision(
                action="SELL",
                side="SHORT",
            )

        return TradeDecision(
            action="NONE",
            side="NONE",
        )