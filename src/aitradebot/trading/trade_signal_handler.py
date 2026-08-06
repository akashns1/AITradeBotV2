from aitradebot.application.events import TradeSignalEvent
from aitradebot.trading.trade_coordinator import TradeCoordinator


class TradeSignalHandler:

    def __init__(
        self,
        trade_coordinator: TradeCoordinator,
        paper_trade_engine,
    ):
        self._trade_coordinator = trade_coordinator
        self._paper_trade_engine = paper_trade_engine

    def handle(
        self,
        event: TradeSignalEvent,
    ) -> None:

        if not self._trade_coordinator.can_enter_trade(
            event.timestamp,
        ):
            return

        self._paper_trade_engine.execute(event)