class CandleBuilderError(Exception):
    """Base exception for candle builder."""


class InvalidInstrumentError(CandleBuilderError):
    """Tick belongs to a different instrument."""


class OutOfOrderTickError(CandleBuilderError):
    """Tick timestamp is earlier than the last processed tick."""
