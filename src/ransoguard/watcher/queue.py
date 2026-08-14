import threading
from queue import Queue
from pathlib import Path

class FileQueue:
    def __init__(self):
        self._queue: Queue = Queue()
        self._modification_counts = {}
        self._lock = threading.Lock()

    def put(self, file_path: Path) -> int:
        path_str = str(file_path)

        with self._lock:
            count = self._modification_counts.get(path_str, 0) + 1
            self._modification_counts[path_str] = count

        self._queue.put(file_path)
        return count

    def get(self):
        return self._queue.get()

    def task_done(self):
        self._queue.task_done()

    def get_modification_count(self, file_path: Path) -> int:
        path_str = str(file_path)
        with self._lock:
            return self._modification_counts.get(path_str, 0)

    def clear_count(self, file_path: Path):
        path_str = str(file_path)
        with self._lock:
            if path_str in self._modification_counts:
                del self._modification_counts[path_str]