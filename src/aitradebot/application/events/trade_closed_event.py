from dataclasses import dataclass

from aitradebot.trading.trade import Trade


@dataclass(frozen=True)
class TradeClosedEvent:
    trade: Trade