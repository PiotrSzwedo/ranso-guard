from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent


class EventHandler(FileSystemEventHandler):
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        pass