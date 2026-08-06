from __future__ import annotations

from datetime import datetime, timedelta

from aitradebot.trading.trade import Trade


class RiskManager:
    """
    Controls whether the bot is allowed to open
    a new trade.

    Responsibilities:
    - Daily profit target
    - Daily stop loss
    - Cooldown period
    """

    def __init__(
        self,
        daily_target_points: float,
        daily_stop_loss_points: float,
        cooldown_minutes: int,
    ) -> None:

        self._daily_target_points = daily_target_points
        self._daily_stop_loss_points = daily_stop_loss_points
        self._cooldown = timedelta(
            minutes=cooldown_minutes,
        )

        self._net_points = 0.0
        self._last_trade_closed_at: datetime | None = None

    # ---------------------------------------------------------

    @property
    def net_points(self) -> float:
        return self._net_points

    # ---------------------------------------------------------

    def can_trade(
        self,
        now: datetime,
    ) -> bool:

        if self.daily_target_hit:
            return False

        if self.daily_stop_hit:
            return False

        if self.cooldown_active(now):
            return False

        return True

    # ---------------------------------------------------------

    def record_trade(
        self,
        trade: Trade,
        closed_at: datetime,
    ) -> None:

        self._net_points += trade.profit_loss

        self._last_trade_closed_at = closed_at

    # ---------------------------------------------------------

    @property
    def daily_target_hit(self) -> bool:

        return (
            self._net_points
            >= self._daily_target_points
        )

    # ---------------------------------------------------------

    @property
    def daily_stop_hit(self) -> bool:

        return (
            self._net_points
            <= -self._daily_stop_loss_points
        )

    # ---------------------------------------------------------

    def cooldown_active(
        self,
        now: datetime,
    ) -> bool:

        if self._last_trade_closed_at is None:
            return False

        return (
            now
            < self._last_trade_closed_at
            + self._cooldown
        )