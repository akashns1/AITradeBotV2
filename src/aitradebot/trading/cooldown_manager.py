from datetime import datetime, timedelta


class CooldownManager:

    def __init__(
        self,
        cooldown: timedelta,
    ):
        self._cooldown = cooldown
        self._last_trade_closed = None

    def trade_closed(
        self,
        when: datetime,
    ) -> None:
        self._last_trade_closed = when

    def is_ready(
        self,
        now: datetime,
    ) -> bool:

        if self._last_trade_closed is None:
            return True

        return (
            now - self._last_trade_closed
        ) >= self._cooldown