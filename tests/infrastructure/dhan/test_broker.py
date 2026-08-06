from aitradebot.infrastructure.dhan.broker import Broker


def test_broker_has_api():

    broker = Broker()

    assert broker.api is not None