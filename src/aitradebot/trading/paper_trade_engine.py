from aitradebot.signals.signal_generator import TradingSignal

from aitradebot.trading.trade import Trade
from aitradebot.signals.signal_generator import TradingSignal
from aitradebot.trading.position import Position
from aitradebot.trading.trade import Trade
from aitradebot.trading.position_manager import PositionManager
from aitradebot.trading.trade_factory import TradeFactory
from aitradebot.trading.exit_reason import ExitReason
from aitradebot.trading.position_factory import PositionFactory

class PaperTradeEngine:
    def __init__(self):
        self.position: Position | None = None
        self.trade_history = []
        self.position_manager = PositionManager()
        self.trade_factory = TradeFactory()
        self.position_factory = PositionFactory()
    @property
    def has_open_position(self) -> bool:
        return self.position is not None

    def process(
        self,
        signal: TradingSignal,
        current_price: float,
        stop_loss: float,
        risk_reward: float = 2.0,
        quantity: int = 1
    ):
        if self.position is not None:
            return

        if signal.action == "BUY":
            self.position = self.position_factory.create(
            side="LONG",
            entry_price=current_price,
            stop_loss=stop_loss,
            risk_reward=risk_reward,
            quantity=quantity,
        )

        elif signal.action == "SELL":
            self.position = self.position_factory.create(
            side="SHORT",
            entry_price=current_price,
            stop_loss=stop_loss,
            risk_reward=risk_reward,
            quantity=quantity,
        )

    

    def close_position(self, exit_price: float):
        if self.position is None:
            return

        trade = self.trade_factory.create_trade(
            self.position,
            exit_price,
        )

        self.trade_history.append(trade)

        self.position = None

    def on_price_update(self, current_price: float):
        if self.position is None:
            return

        reason = self.position_manager.should_close(
            self.position,
            current_price,
        )

        if reason != ExitReason.NONE:
            self.close_position(current_price)