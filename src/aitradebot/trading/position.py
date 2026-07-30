from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    side: str
    entry_price: float
    stop_loss: float
    target_price: float
    quantity: int = 1
