from aitradebot.trading.position import Position


class PositionFactory:

    def create(
        self,
        side: str,
        entry_price: float,
        stop_loss: float,
        risk_reward: float,
        quantity: int = 1,
    ) -> Position:
        
        risk = abs(entry_price - stop_loss)

        if side == "LONG":
            target = entry_price + (risk * risk_reward)
        else:
            target = entry_price - (risk * risk_reward)

        return Position(
            side=side,
            entry_price=entry_price,
            stop_loss=stop_loss,
            target_price=target,
            quantity=quantity,
        )