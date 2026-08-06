from aitradebot.infrastructure.dhan.instrument import BrokerInstrument
from aitradebot.market.option_resolver import OptionResolver


class FakeRepository:

    def get_option(self, **kwargs):

        return BrokerInstrument(
            security_id="123",
            exchange_segment=2,
            instrument_type="OP",
            symbol="NIFTY CE",
        )


def test_resolve_option():

    resolver = OptionResolver(
        FakeRepository(),
    )

    instrument = resolver.resolve(
        underlying="NIFTY",
        strike=24500,
        option_type="CE",
    )

    assert instrument.security_id == "123"