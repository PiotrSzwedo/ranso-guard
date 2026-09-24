import math
from collections import Counter
from difflib import Match

from watcher.queue import FileQueue


class Worker:
    def __init__(self, identification_chrset: str, file_queue: FileQueue):
        self.id = identification_chrset
        self.queue = file_queue

    def calculate_the_entropy(self, file_path: str):
        with open(file_path, "rb") as f:
            data = f.read()

        if not data:
            return 0.0

        counts = Counter(data)
        size: int = len(data)

        result = 0

        for count in counts.values():
            # H = ∑i(pi(−log⁡2pi))
            p = count / size
            result += p * (-1 * math.log2(p))

        return result