import threading
import time
from pathlib import Path
from queue import Queue


class FileQueue:
    def __init__(self):
        self._queue: Queue = Queue()
        self._modification_timestamps = {}
        self._total_pending_changes = {}
        self._lock = threading.Lock()

    def _is_in_queue_already(self, file_path: Path) -> bool:
        with self._lock:
            return file_path in self._queue.queue

    def put(self, file_path: Path) -> int:
        path_str = str(file_path)
        now = time.time()
        time_window = 5.0

        with self._lock:
            timestamps = self._modification_timestamps.get(path_str, [])
            timestamps = [t for t in timestamps if now - t <= time_window]
            timestamps.append(now)

            self._modification_timestamps[path_str] = timestamps
            self._total_pending_changes[path_str] = self._total_pending_changes.get(path_str, 0) + 1

        if not self._is_in_queue_already(file_path):
            self._queue.put(file_path)

        return len(timestamps)

    def get(self):
        return self._queue.get()

    def task_done(self):
        self._queue.task_done()

    def get_modification_count(self, file_path: Path) -> int:
        path_str = str(file_path)
        with self._lock:
            return len(self._modification_timestamps.get(path_str, []))

    def get_total_pending_changes(self, file_path: Path) -> int:
        path_str = str(file_path)
        with self._lock:
            return self._total_pending_changes.get(path_str, 0)

    def clear_count(self, file_path: Path):
        path_str = str(file_path)
        with self._lock:
            self._modification_timestamps.pop(path_str, None)
            self._total_pending_changes.pop(path_str, None)
