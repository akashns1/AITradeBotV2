from aitradebot.trading.trading_pipeline import TradingPipeline


def test_process_returns_trade_decision(create_candle):
    candles = [
        create_candle(100),
        create_candle(105),
        create_candle(101),
        create_candle(110),
        create_candle(106),
    ]

    pipeline = TradingPipeline()

    decision = pipeline.process(candles)

    assert decision is not None