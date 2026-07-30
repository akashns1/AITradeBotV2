# src/aitradebot/signals/signal_type.py

from enum import StrEnum


class SignalType(StrEnum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
