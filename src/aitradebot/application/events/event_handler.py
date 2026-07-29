from __future__ import annotations

from abc import ABC, abstractmethod

from aitradebot.application.events.event import Event


class EventHandler(ABC):
    """
    Base class for all event handlers.
    """

    @abstractmethod
    def handle(self, event: Event) -> None:
        """Handle an event."""
