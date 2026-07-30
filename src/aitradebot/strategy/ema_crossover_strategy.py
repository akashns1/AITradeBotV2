from aitradebot.signals.signal import Signal
from aitradebot.signals.signal_type import SignalType
from aitradebot.strategy.base_strategy import BaseStrategy
from aitradebot.strategy.market_context import MarketContext


class EMACrossoverStrategy(BaseStrategy):
    def evaluate(
        self,
        context: MarketContext,
    ) -> Signal | None:

        ema20_prev = context.indicators["EMA20_PREV"]
        ema50_prev = context.indicators["EMA50_PREV"]
        ema20 = context.indicators["EMA20"]
        ema50 = context.indicators["EMA50"]

        # Bullish crossover
        if ema20_prev < ema50_prev and ema20 > ema50:
            return Signal(
                signal_type=SignalType.BUY,
                instrument=context.candle.instrument,
                timeframe=context.candle.timeframe,
                timestamp=context.candle.end_time,
            )

        # Bearish crossover
        if ema20_prev > ema50_prev and ema20 < ema50:
            return Signal(
                signal_type=SignalType.SELL,
                instrument=context.candle.instrument,
                timeframe=context.candle.timeframe,
                timestamp=context.candle.end_time,
            )

        return None