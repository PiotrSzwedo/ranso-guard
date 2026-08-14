from watchdog.events import DirCreatedEvent, FileCreatedEvent, DirDeletedEvent, FileDeletedEvent, DirModifiedEvent, \
    FileModifiedEvent, DirMovedEvent, FileMovedEvent, PatternMatchingEventHandler, FileSystemEvent

from watcher.queue import FileQueue


class EventHandler(PatternMatchingEventHandler):
    def __init__(self, ignore_patterns: list[str], file_queue: FileQueue):
        self.file_queue: FileQueue = file_queue
        super().__init__(
            ignore_patterns=ignore_patterns
        )

    def _add_to_queue(self, event: FileSystemEvent):
        if not event.is_directory:
            self.file_queue.put(event.src_path)

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        self._add_to_queue(event)

    def on_deleted(self, event: DirDeletedEvent | FileDeletedEvent) -> None:
        if not event.is_directory:
            self.file_queue.clear_count(event.src_path)

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        self._add_to_queue(event)

    def on_moved(self, event: DirMovedEvent | FileMovedEvent) -> None:
        if not event.is_directory:
            self.file_queue.put(event.dest_path)
