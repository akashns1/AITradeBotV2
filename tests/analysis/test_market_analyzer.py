from datetime import UTC, datetime

from aitradebot.analysis.market_analyzer import MarketAnalyzer
from aitradebot.analysis.trend import Trend
from aitradebot.analysis.trend_strength import TrendStrength
from aitradebot.domain.market.candle import Candle
from aitradebot.domain.common import Instrument, TimeFrame
from aitradebot.strategy.market_context import MarketContext


def test_market_analyzer_classifies_strong_uptrend() -> None:
    candle = Candle(
        instrument=Instrument("NIFTY", "NSE"),
        timeframe=TimeFrame.TWO_MINUTES,
        open=100,
        high=105,
        low=99,
        close=104,
        volume=100,
        start_time=datetime(2026, 1, 1, 9, 15, tzinfo=UTC),
        end_time=datetime(2026, 1, 1, 9, 17, tzinfo=UTC),
    )

    context = MarketContext(
        candle=candle,
        indicators={
            "EMA8": 104.0,
            "EMA20": 100.0,
            "ATR": 2.0,
        },
    )

    analyzer = MarketAnalyzer()

    analysis = analyzer.analyze(context)

    assert analysis.trend is Trend.UP
    assert analysis.strength is TrendStrength.STRONG
    assert analysis.ema_gap == 4.0
    assert analysis.atr == 2.0