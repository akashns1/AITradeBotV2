from enum import StrEnum


class EventType(StrEnum):
    """
    Application event names.
    """

    TICK_RECEIVED = "tick_received"
    CANDLE_COMPLETED = "candle_completed"
    SIGNAL_GENERATED = "signal_generated"
    ORDER_CREATED = "order_created"
    ORDER_FILLED = "order_filled"
    POSITION_OPENED = "position_opened"
    POSITION_CLOSED = "position_closed"
