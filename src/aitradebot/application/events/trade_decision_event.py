from dataclasses import dataclass

from aitradebot.application.events.event import Event
from aitradebot.trading.trade_decision_engine import TradeDecision


@dataclass(frozen=True)
class TradeDecisionEvent(Event):
    decision: TradeDecision