from aitradebot.trading.position import Position
from aitradebot.trading.trade import Trade


class TradeFactory:

    def create_trade(
        self,
        position: Position,
        exit_price: float,
    ) -> Trade:

        if position.side == "LONG":
            profit_loss = (exit_price - position.entry_price)* position.quantity
        else:
            profit_loss = (position.entry_price - exit_price)* position.quantity

        return Trade(
            side=position.side,
            entry_price=position.entry_price,
            exit_price=exit_price,
            profit_loss=profit_loss,
        )