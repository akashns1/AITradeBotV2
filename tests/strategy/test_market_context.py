from datetime import UTC, datetime

from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.domain.market import Candle
from aitradebot.strategy.market_context import MarketContext


def test_market_context_can_be_created() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=110,
        low=95,
        close=105,
        volume=100,
        start_time=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 2, tzinfo=UTC),
    )

    context = MarketContext(
        candle=candle,
    )

    assert context.candle == candle
