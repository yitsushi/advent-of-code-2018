from typing import List


class SleepPeriod:
    guard_id: int
    _from: int
    _to: int

    def __init__(self, _guard_id: int):
        self.guard_id = _guard_id

    def set_from_minute(self, minutes: int):
        self._from = minutes

    def set_to_minute(self, minutes: int):
        self._to = minutes

    def duration(self) -> int:
        return self._to - self._from

    def array(self) -> List[int]:
        return list(range(self._from, self._to))
