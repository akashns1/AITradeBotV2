from unittest.mock import Mock

from aitradebot.domain.market.candle import Candle
from aitradebot.trading.replay_engine import ReplayEngine


def test_replay_engine_processes_all_spot_candles():
    signal_generator = Mock()
    trade_engine = Mock()

    replay = ReplayEngine(
        signal_generator=signal_generator,
        trade_engine=trade_engine,
    )

    candles = [
        Candle(open=1, high=2, low=1, close=2),
        Candle(open=2, high=3, low=2, close=3),
        Candle(open=3, high=4, low=3, close=4),
    ]

    replay.replay(candles)

    assert signal_generator.generate.call_count == 3