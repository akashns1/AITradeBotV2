from datetime import datetime
from datetime import timezone
from aitradebot.application.events.trade_decision_event import (
    TradeDecisionEvent,
)
from aitradebot.trading.active_session_filter import (
    ActiveSessionFilter,
)
from aitradebot.trading.cooldown_manager import (
    CooldownManager,
)
from aitradebot.trading.paper_trade_engine import (
    PaperTradeEngine,
)

from aitradebot.trading.risk_manager import RiskManager

class TradeCoordinator:

    def __init__(
        self,
        session_filter: ActiveSessionFilter,
        cooldown_manager: CooldownManager,
        risk_manager: RiskManager,
        paper_trade_engine: PaperTradeEngine,
    ) -> None:

        self._session_filter = session_filter
        self._cooldown_manager = cooldown_manager
        self._risk_manager = risk_manager
        self._paper_trade_engine = paper_trade_engine

    
    
    def can_enter_trade(
        self,
        now,
    ) -> bool:

        if not self._session_filter.is_active(now):
            return False

        if not self._cooldown_manager.is_ready(now):
            return False

        if not self._risk_manager.can_trade(now):
            return False

        if self._paper_trade_engine.has_open_position:
            return False

        return True


    def handle_trade_decision(
        self,
        event: TradeDecisionEvent,
    ) -> None:

        now = event.candle.end_time

        print("\n========== TRADE COORDINATOR ==========")
        print(f"Time               : {now}")
        print(
            f"Session Active     : "
            f"{self._session_filter.is_active(now)}"
        )
        print(
            f"Cooldown Ready     : "
            f"{self._cooldown_manager.is_ready(now)}"
        )
        print(
            f"Risk Manager       : "
            f"{self._risk_manager.can_trade(now)}"
        )
        print(
            f"Open Position      : "
            f"{self._paper_trade_engine.has_open_position}"
        )
        print("=======================================")

        if not self.can_enter_trade(now):
            print("Trade Rejected")
            return

        print("Trade Approved")

        self._paper_trade_engine.handle_trade_decision(
            event,
        )