from aitradebot.application.bootstrap import create_application


def test_create_application():
    app = create_application()

    assert app.event_bus is not None
    assert app.market_engine is not None
    assert app.trading_pipeline is not None