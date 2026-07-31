from watchdog.events import DirCreatedEvent, FileCreatedEvent, DirDeletedEvent, FileDeletedEvent, DirModifiedEvent, FileModifiedEvent, DirMovedEvent, FileMovedEvent, PatternMatchingEventHandler
from action_handler import ActionHandler


class EventHandler(PatternMatchingEventHandler):
    def __init__(self, ignore_patterns: list[str], actions: ActionHandler):
        super().__init__(
            ignore_patterns=ignore_patterns
        )

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        pass