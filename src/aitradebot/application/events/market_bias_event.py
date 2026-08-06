from dataclasses import dataclass

from aitradebot.analysis.market_bias import MarketBias
from aitradebot.application.events.event import Event
from aitradebot.domain.trading import TradingInstrument


@dataclass(frozen=True, slots=True)
class MarketBiasEvent(Event):
    bias: MarketBias
    spot_price: float
    trading_instrument: TradingInstrument