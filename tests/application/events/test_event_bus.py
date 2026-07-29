from aitradebot.application.events.event import Event
from aitradebot.application.events.event_bus import EventBus


class DummyEvent(Event):
    pass


def test_publish_calls_subscriber() -> None:
    bus = EventBus()

    received = []

    def handler(event: Event) -> None:
        received.append(event)

    bus.subscribe(DummyEvent, handler)

    event = DummyEvent()

    bus.publish(event)

    assert received == [event]
