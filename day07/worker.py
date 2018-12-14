from typing import Any


class Worker:
    item: Any
    busy_until: int
    default_task_length: int

    def __init__(self, default_task_length: int):
        self.default_task_length = default_task_length
        self.busy_until = -1
        self.item = None

    def is_busy(self, time: int) -> bool:
        return time <= self.busy_until

    def is_ready(self, time: int):
        return self.item is not None and time >= self.busy_until

    def done(self) -> Any:
        # print(f'Task "{self.item}" is done [{id(self)}]')
        _task = self.item
        self.item = None
        return _task

    def assign(self, _task: Any, _current_time: int):
        self.item = _task
        self.busy_until = _current_time + self.default_task_length + (ord(_task) - 64) - 1
        # print(f'Task "{_task}" assigned to {id(self)} -> {self.busy_until}')
