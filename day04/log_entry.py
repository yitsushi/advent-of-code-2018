class LogEntry:
    time = None
    guard_id: int
    begins: int
    sleep: int
    wake: int

    def __init__(self):
        self.time = None
        self.guard_id = None
        self.begins = None
        self.sleep = None
        self.wake = None

    def __gt__(self, other) -> bool:
        return self.time > other.time

    def __eq__(self, other) -> bool:
        return self.time == other.time
