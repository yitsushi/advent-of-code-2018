#!/usr/bin/env python3

import re, operator, itertools
from datetime import datetime

class SleepPeriod():
    guardId = None
    _from = None
    _to = None

    def __init__(self, guardId):
        self.guardId = guardId

    def fromMinute(self, minutes):
        self._from = minutes

    def toMinute(self, minutes):
        self._to = minutes

    def duration(self):
        return self._to - self._from

    def array(self):
        return list(range(self._from, self._to))

class LogEntry():
    BASE_FORMAT = r'^\[([^\]]+)\] (.*)$'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M'

    time = None
    guardId = None
    begins = False
    sleep = False
    wake = False

    def __init__(self, s):
        (ts, message) = re.search(LogEntry.BASE_FORMAT, s).groups()

        self.time = datetime.strptime(ts, LogEntry.DATETIME_FORMAT)

        parts = message.split(' ')

        if parts[0] == 'Guard':
            self.guardId = int(parts[1][1:])
        elif parts[0] == 'wakes':
            self.wake = True
        elif parts[0] == 'falls':
            self.sleep = True
        else:
            print(message)

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time

with open('../input') as f:
    lines = f.read().split('\n')
    entries = [LogEntry(entry) for entry in lines if entry != '']

entries.sort()

duration = None
durations = []

for entry in entries:
    if entry.guardId != None:
        duration = SleepPeriod(entry.guardId)
    elif entry.sleep:
        duration.fromMinute(entry.time.minute)
    elif entry.wake:
        duration.toMinute(entry.time.minute)
        durations.append(duration)
        duration = SleepPeriod(duration.guardId)

summary = {}

for entry in durations:
    id = str(entry.guardId)
    summary[id] = summary.get(id, 0) + entry.duration()


minutes = sorted((m, s.guardId) for s in durations for m in s.array())
groups = itertools.groupby(minutes, key=operator.itemgetter(0))

summary_minutes = {}
for m, it in groups:
    guards = itertools.groupby(it)
    summary_guards = {}
    for g, it in guards:
        summary_guards[str(g[1])] = sum(1 for x in it)
    summary_minutes[str(m)] = max(summary_guards.items(), key=operator.itemgetter(1))

# minute, guard, times
max_entry = (0, 0, 0)

for m in summary_minutes:
    if summary_minutes[m][1] > max_entry[2]:
        max_entry = (int(m), int(summary_minutes[m][0]), summary_minutes[m][1])

print(max_entry[0] * max_entry[1])
