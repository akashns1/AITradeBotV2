from aitradebot.application.events.trade_decision_event import (
    TradeDecisionEvent,
)
from aitradebot.trading.exit_reason import ExitReason
from aitradebot.trading.position import Position
from aitradebot.trading.position_factory import PositionFactory
from aitradebot.trading.position_manager import PositionManager
from aitradebot.trading.trade import Trade
from aitradebot.trading.trade_decision_engine import TradeDecision
from aitradebot.trading.trade_factory import TradeFactory
from aitradebot.trading.trailing_stop_manager import (
    TrailingStopManager,
)
from aitradebot.application.events.event_bus import (
    EventBus,
)

class PaperTradeEngine:
    """
    Executes paper trades from TradeDecisionEvents.
    """

    def __init__(
            self,
            event_bus: EventBus,
        ) -> None:

        self._event_bus = event_bus

        self.position: Position | None = None
        self.trade_history: list[Trade] = []

        self.position_manager = PositionManager()
        self.trade_factory = TradeFactory()
        self.position_factory = PositionFactory()
        self.trailing_stop_manager = TrailingStopManager()

    # ---------------------------------------------------------

    @property
    def has_open_position(self) -> bool:
        return self.position is not None

    # ---------------------------------------------------------

    def process(
        self,
        decision: TradeDecision,
        current_price: float,
        stop_loss: float,
        risk_reward: float = 2.0,
        quantity: int = 1,
    ) -> None:

        if self.position is not None:

            print("PaperTradeEngine: Position already open.")

            return

        if decision.action != "BUY":
            return

        self.position = self.position_factory.create(
            side="LONG",
            entry_price=current_price,
            stop_loss=stop_loss,
            risk_reward=risk_reward,
            quantity=quantity,
        )

        print("\n" + "=" * 50)
        print("PAPER TRADE OPENED")
        print("=" * 50)

        print(f"Option Type : {decision.option_type}")
        print(f"Position    : {self.position.side}")
        print(f"Entry      : {self.position.entry_price}")
        print(f"Stop Loss  : {self.position.stop_loss}")
        print(f"Target     : {self.position.target_price}")
        print(f"Quantity   : {self.position.quantity}")

        print("=" * 50)

    # ---------------------------------------------------------

    def close_position(
        self,
        exit_price: float,
    ) -> None:

        if self.position is None:
            return

        trade = self.trade_factory.create_trade(
            self.position,
            exit_price,
        )

        self.trade_history.append(trade)
        self.position = None
        print("\n" + "=" * 50)
        print("PAPER TRADE CLOSED")
        print("=" * 50)
        print(f"Direction  : {trade.side}")
        print(f"Entry      : {trade.entry_price}")
        print(f"Exit       : {trade.exit_price}")
        print(f"PnL        : {trade.profit_loss:.2f}")
        print("=" * 50)

        

    # ---------------------------------------------------------

    def on_price_update(
        self,
        current_price: float,
    ) -> None:

        if self.position is None:
            return

        self.position = self.trailing_stop_manager.update(
            self.position,
            current_price,
        )

        reason = self.position_manager.should_close(
            self.position,
            current_price,
        )

        if reason != ExitReason.NONE:

            print(f"Exit Reason : {reason}")

            self.close_position(
                current_price,
            )
        if self.position is not None:
            print("\nPosition Update")
            print(f"Current Price : {current_price}")
            print(f"Trailing SL   : {self.position.stop_loss}")
    # ---------------------------------------------------------

    def handle_trade_decision(
        self,
        event: TradeDecisionEvent,
    ) -> None:
        """
        Handles a TradeDecisionEvent from the TradingPipeline.
        """

        print("\n========== PAPER TRADE ENGINE ==========")
        print("Decision Received")
        print(event.decision)
        print(f"Entry Price : {event.candle.close}")
        print(f"Stop Loss   : {event.stop_loss}")
        print("========================================")

        self.process(
            decision=event.decision,
            current_price=event.candle.close,
            stop_loss=event.stop_loss,
        )