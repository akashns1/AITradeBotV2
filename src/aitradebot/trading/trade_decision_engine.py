from dataclasses import dataclass

from aitradebot.analysis.market_structure_analyzer import MarketStructure


@dataclass(frozen=True)
class TradeDecision:
    action: str  # BUY | SELL | NONE


class TradeDecisionEngine:

    def decide(self, structure: MarketStructure) -> TradeDecision:
        if structure.is_bullish_bos:
            return TradeDecision(action="BUY")

        if structure.is_bearish_bos:
            return TradeDecision(action="SELL")

        return TradeDecision(action="NONE")