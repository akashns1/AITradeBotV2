class EventBusError(Exception):
    """Base event bus exception."""


class EventHandlerAlreadyRegistered(EventBusError):
    """Handler already exists."""


class EventHandlerNotFound(EventBusError):
    """Handler not found."""
