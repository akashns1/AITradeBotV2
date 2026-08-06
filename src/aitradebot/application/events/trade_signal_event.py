from dataclasses import dataclass
from datetime import datetime

from aitradebot.analysis.market_direction import MarketDirection
from aitradebot.application.events.event import Event
from aitradebot.domain.option import OptionContract
from aitradebot.domain.trading import TradingInstrument


@dataclass(frozen=True, slots=True)
class TradeSignalEvent(Event):
    trading_instrument: TradingInstrument
    option_contract: OptionContract
    direction: MarketDirection
    entry_price: float
    timestamp: datetime