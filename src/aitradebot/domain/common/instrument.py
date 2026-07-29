from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Instrument:
    symbol: str
    exchange: str

    @property
    def full_symbol(self) -> str:
        return f"{self.exchange}:{self.symbol}"
