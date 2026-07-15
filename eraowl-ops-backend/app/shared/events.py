from collections import defaultdict
from typing import Any, Callable

_subscribers: dict[str, list[Callable[[dict[str, Any]], None]]] = defaultdict(list)


def publish(event_type: str, payload: dict[str, Any]) -> None:
    for handler in _subscribers.get(event_type, []):
        handler(payload)


def subscribe(event_type: str, handler: Callable[[dict[str, Any]], None]) -> None:
    _subscribers[event_type].append(handler)
