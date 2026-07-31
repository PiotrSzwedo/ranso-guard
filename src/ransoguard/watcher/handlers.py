from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent


class EventHandler(FileSystemEventHandler):
    def __init__(self, ignore_patterns: list[str]):
        super().__init__(
            ignore_patterns=ignore_patterns
        )

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        pass