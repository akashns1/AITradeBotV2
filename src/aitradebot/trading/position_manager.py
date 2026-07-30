from aitradebot.trading.exit_reason import ExitReason
from aitradebot.trading.position import Position


class PositionManager:

    def should_close(
        self,
        position: Position,
        current_price: float,
    ) -> ExitReason:

        if position.side == "LONG":
            if current_price <= position.stop_loss:
                return ExitReason.STOP_LOSS

            if current_price >= position.target_price:
                return ExitReason.TAKE_PROFIT

        if position.side == "SHORT":
            if current_price >= position.stop_loss:
                return ExitReason.STOP_LOSS

            if current_price <= position.target_price:
                return ExitReason.TAKE_PROFIT

        return ExitReason.NONE