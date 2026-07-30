from dataclasses import dataclass


@dataclass(frozen=True)
class Trade:
    side: str
    entry_price: float
    exit_price: float
    profit_loss: float