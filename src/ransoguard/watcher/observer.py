from watchdog.observers import Observer


class DirectoryObserver(Observer):
    def __init__(self, event_handler, path_to_observe):
        super().__init__()
        self.event_handler = event_handler
        self.path_to_observe = path_to_observe

    def observer_start(self):
        self.schedule(
            self.event_handler,
            self.path_to_observe,
            recursive=True
        )
        self.start()

    def observer_stop(self):
        self.stop()
        self.join()