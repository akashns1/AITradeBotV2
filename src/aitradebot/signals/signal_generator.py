from dataclasses import dataclass

from aitradebot.analysis.market_structure_analyzer import MarketStructure


@dataclass(frozen=True)
class TradingSignal:
    action: str


class SignalGenerator:
    def generate(self, structure: MarketStructure) -> TradingSignal:
        if structure.is_bullish_bos:
            return TradingSignal(action="BUY")

        if structure.is_bearish_bos:
            return TradingSignal(action="SELL")

        return TradingSignal(action="WAIT")