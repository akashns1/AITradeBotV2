"""
Live Market Adapter

Bridges the Dhan LiveFeed, MarketEngine and PaperTradeEngine.
"""

from aitradebot.infrastructure.dhan.tick_mapper import (
    DhanTickMapper,
)
from aitradebot.market.market_engine import (
    MarketEngine,
)
from aitradebot.trading.paper_trade_engine import (
    PaperTradeEngine,
)


class LiveMarketAdapter:
    """
    Receives raw Dhan ticks and forwards them to:
      1. MarketEngine (build candles)
      2. PaperTradeEngine (manage open trades)
    """

    def __init__(
        self,
        mapper: DhanTickMapper,
        market_engine: MarketEngine,
        paper_trade_engine: PaperTradeEngine,
    ) -> None:

        self._mapper = mapper
        self._market_engine = market_engine
        self._paper_trade_engine = paper_trade_engine

    # ---------------------------------------------------------

    def on_tick(
        self,
        raw_tick: dict,
    ) -> None:

        try:

            # Ignore non-price messages
            if raw_tick.get("type") != "Ticker Data":
                return

            tick = self._mapper.map(
                raw_tick,
            )

            # Feed Market Engine
            self._market_engine.process_tick(
                tick,
            )

            # Update any open paper trade
            self._paper_trade_engine.on_price_update(
                tick.price,
            )

        except Exception as ex:

            print("\n========== LIVE MARKET ADAPTER ERROR ==========")
            print(ex)
            print("===============================================")

            raise