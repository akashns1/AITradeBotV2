from dataclasses import replace

from aitradebot.trading.position import Position


class TrailingStopManager:

    def update(
        self,
        position: Position,
        current_price: float,
    ) -> Position:

        if position.side == "LONG":
            new_stop = max(
                position.stop_loss,
                current_price - 3.0,
            )

            return self._move_stop(
                position,
                new_stop,
            )

        elif position.side == "SHORT":
            new_stop = min(
                position.stop_loss,
                current_price + 3.0,
            )

            return self._move_stop(
                position,
                new_stop,
            )

        return position

    def update_to_level(
        self,
        position: Position,
        level: float,
    ) -> Position:

        if position.side == "LONG":
            new_stop = max(position.stop_loss, level)

        elif position.side == "SHORT":
            new_stop = min(position.stop_loss, level)

        else:
            return position

        return self._move_stop(
            position,
            new_stop,
        )
    def _move_stop(
        self,
        position: Position,
        new_stop: float,
    ) -> Position:
        return replace(
            position,
            stop_loss=new_stop,
        )