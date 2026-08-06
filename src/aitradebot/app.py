from aitradebot.application.bootstrap import create_application

from aitradebot.infrastructure.dhan.broker import Broker
from aitradebot.infrastructure.dhan.instrument_repository import (
    InstrumentRepository,
)
from aitradebot.infrastructure.dhan.spot_price_service import (
    SpotPriceService,
)

from aitradebot.market.atm_strike_calculator import (
    ATMStrikeCalculator,
)
from aitradebot.market.strike_selector import (
    StrikeSelector,
)
from aitradebot.market.option_resolver import (
    OptionResolver,
)
from aitradebot.infrastructure.dhan.live_feed import LiveFeed
from aitradebot.infrastructure.dhan.instrument_mapper import (
    InstrumentMapper,
)
from aitradebot.infrastructure.dhan.tick_mapper import (
    DhanTickMapper,
)
from aitradebot.infrastructure.dhan.live_market_adapter import (
    LiveMarketAdapter,
)
from aitradebot.domain.common import TimeFrame
import logging

logging.basicConfig(
    filename="aitradebot.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def main() -> None:

    print("=" * 50)
    print("AITradeBot V2")
    print("=" * 50)

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    app = create_application()

    # --------------------------------------------------
    # Broker
    # --------------------------------------------------

    broker = Broker()

    # --------------------------------------------------
    # Instrument Repository
    # --------------------------------------------------

    repository = InstrumentRepository()

    # --------------------------------------------------
    # Resolve NIFTY Spot Instrument
    # --------------------------------------------------

    nifty = repository.get_underlying(
        "NIFTY",
    )

    if nifty is None:
        raise RuntimeError(
            "Unable to resolve NIFTY."
        )

    print("\nSpot Instrument")
    print(nifty)

    # --------------------------------------------------
    # Spot Price
    # --------------------------------------------------

    spot_service = SpotPriceService(
        broker=broker,
    )

    spot_price = spot_service.get_price(
        nifty,
    )

    print(f"\nSpot Price : {spot_price}")

    # --------------------------------------------------
    # ATM Strike
    # --------------------------------------------------

    atm_calculator = ATMStrikeCalculator()

    atm = atm_calculator.calculate(
        spot_price=spot_price,
        strike_step=50,
    )

    print(f"\nATM Strike : {atm}")

    # --------------------------------------------------
    # Strike Selection
    # --------------------------------------------------

    strike_selector = StrikeSelector()

    ce_strike = strike_selector.select(
        atm=atm,
        signal="BULLISH",
        option_style="ATM",
        strike_step=50,
    )

    pe_strike = strike_selector.select(
        atm=atm,
        signal="BEARISH",
        option_style="ATM",
        strike_step=50,
    )

    print(f"CE Strike : {ce_strike}")
    print(f"PE Strike : {pe_strike}")

    # --------------------------------------------------
    # Resolve Option Contracts
    # --------------------------------------------------

    resolver = OptionResolver(
        repository,
    )

    ce = resolver.resolve(
        underlying="NIFTY",
        strike=ce_strike,
        option_type="CE",
    )

    pe = resolver.resolve(
        underlying="NIFTY",
        strike=pe_strike,
        option_type="PE",
    )

    print("\nResolved CE")
    print(ce)

    print("\nResolved PE")
    print(pe)
    # --------------------------------------------------
    # Register Instruments
    # --------------------------------------------------

    instrument_mapper = InstrumentMapper()

    ce_instrument = instrument_mapper.map(ce)
    pe_instrument = instrument_mapper.map(pe)

    app.market_engine.add_instrument(
        ce_instrument,
        TimeFrame.TWO_MINUTES,
    )

    app.market_engine.add_instrument(
        pe_instrument,
        TimeFrame.TWO_MINUTES,
    )

# --------------------------------------------------
# Tick Mapper
# --------------------------------------------------

    instrument_lookup = {
        ce.security_id: ce_instrument,
        pe.security_id: pe_instrument,
    }

    tick_mapper = DhanTickMapper(
        instrument_lookup,
    )

    adapter = LiveMarketAdapter(
        mapper=tick_mapper,
        market_engine=app.market_engine,
        paper_trade_engine=app.paper_trade_engine,
    )



    feed = LiveFeed(
        on_ticks_callback=adapter.on_tick,
    )

    feed.connect(
        contracts=[
            ce,
            pe,
        ]
    )
    print("\n" + "=" * 50)
    print("Startup Completed Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()