from datetime import datetime
import operator
import itertools
from advent_of_code import BaseSolution
from typing import List, Dict, Tuple
from .log_entry import LogEntry
from .sleep_period import SleepPeriod


class Solution(BaseSolution):
    entries: List[LogEntry]
    durations: List[SleepPeriod]
    summary: Dict[int, int]

    def setup(self):
        self.entries = []
        self.durations = []
        self.summary = {}

        (input_file, ) = self.parameters()
        self.__parse_entries(input_file)
        self.__parse_durations()

        for entry in self.durations:
            _id = entry.guard_id
            self.summary[_id] = self.summary.get(_id, 0) + entry.duration()

    def __parse_entries(self, input_file):
        base_format = r'^\[([^\]]+)\] (.*)$'
        for line in self.read_input(input_file):
            entry = LogEntry()

            ts, message = self.parse(line, base_format, (str, str))
            entry.time = datetime.strptime(ts, '%Y-%m-%d %H:%M')

            parts = message.split(' ')
            if parts[0] == 'Guard':
                entry.guard_id = int(parts[1][1:])
            elif parts[0] == 'wakes':
                entry.wake = True
            elif parts[0] == 'falls':
                entry.sleep = True
            else:
                print(message)

            self.entries.append(entry)

        self.entries.sort()

    def __parse_durations(self):
        duration = None

        for entry in self.entries:
            if entry.guard_id is not None:
                duration = SleepPeriod(entry.guard_id)
            elif entry.sleep:
                duration.set_from_minute(entry.time.minute)
            elif entry.wake:
                duration.set_to_minute(entry.time.minute)
                self.durations.append(duration)
                duration = SleepPeriod(duration.guard_id)

    def part1(self):
        slept_the_most: int = max(self.summary.items(), key=operator.itemgetter(1))[0]

        specific = [e for e in self.durations if e.guard_id == slept_the_most]

        minutes = sorted(m for s in specific for m in s.array())
        groups = itertools.groupby(minutes)

        minute_dict: Dict[int, int] = {}
        for m, it in groups:
            minute_dict[m] = sum(1 for x in it)

        most_minute: int = max(minute_dict.items(), key=operator.itemgetter(1))[0]

        return most_minute * slept_the_most

    def part2(self):
        minutes = sorted((m, s.guard_id) for s in self.durations for m in s.array())
        groups = itertools.groupby(minutes, key=operator.itemgetter(0))

        summary_minutes: Dict[int, int] = {}
        for m, gr_it in groups:
            guards = itertools.groupby(gr_it)
            summary_guards = {}
            for g, g_it in guards:
                summary_guards[g[1]] = sum(1 for _ in g_it)
            summary_minutes[m] = max(summary_guards.items(), key=operator.itemgetter(1))

        # minute, guard, times
        max_entry: Tuple[int, int, int] = (0, 0, 0)

        for m in summary_minutes:
            if summary_minutes[m][1] > max_entry[2]:
                max_entry = (m, summary_minutes[m][0], summary_minutes[m][1])

        return max_entry[0] * max_entry[1]
