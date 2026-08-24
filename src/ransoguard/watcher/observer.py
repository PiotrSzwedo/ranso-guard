import os
from pathlib import Path

from watchdog.observers import Observer
from watcher.handlers import EventHandler


class DirectoryObserver(Observer):
    def __init__(self, event_handler, path_to_observe):
        super().__init__()
        self.event_handler: EventHandler = event_handler
        self.path_to_observe: Path = Path(path_to_observe)

    def observer_start(self):
        if self.is_alive():
            raise RuntimeError("Observer is already running")

        if not self.path_to_observe.exists():
            raise FileNotFoundError("Path does not exist")

        if not self.path_to_observe.is_dir():
            raise NotADirectoryError(f"{self.path_to_observe} is not a directory")

        if not os.access(self.path_to_observe, os.R_OK):
            raise PermissionError(f"No read permission for {self.path_to_observe}")

        self.schedule(
            self.event_handler,
            self.path_to_observe,
            recursive=True
        )
        self.start()

    def observer_stop(self):
        self.stop()
        self.join()