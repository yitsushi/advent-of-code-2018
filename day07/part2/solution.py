#!/usr/bin/env python3

import advent_of_code as aoc
from typing import Dict, List


class Worker:
    item = None
    busy_until = -1

    def is_busy(self, time):
        return time <= self.busy_until

    def is_ready(self, time):
        return self.item is not None and time >= self.busy_until

    def done(self):
        print(f'Task "{self.item}" is done [{id(self)}]')
        _task = self.item
        self.item = None
        return _task

    def assign(self, _task, _current_time):
        del task_graph[_task]
        self.item = _task
        self.busy_until = _current_time + task_default_length + (ord(_task) - 64) - 1
        print(f'Task "{_task}" assigned to {id(self)} -> {self.busy_until}')


def done(_task):
    final_sequence.append(_task)
    for t in task_graph:
        if task_graph[t] is not None and _task in task_graph[t]:
            task_graph[t].remove(_task)


task_graph: Dict[str, List[str]] = {}
list_of_tasks: List[str] = []

INSTRUCTION_PATTERN = r'^Step (\w) must be finished before step (\w) can begin.$'
(input_file, number_of_workers, task_default_length) = aoc.parameters(
        (str, int, int),
        ('Input File', 'NUmber of Workers', 'Default Task Length'),
        (None, 5, 60))
for line in aoc.read_input(input_file):
    task1, task2 = aoc.parse(line, INSTRUCTION_PATTERN, (str, str))
    task_graph[task2] = task_graph.get(task2, []) + [task1]
    list_of_tasks.append(task1)
    list_of_tasks.append(task2)

list_of_tasks = sorted(set(list_of_tasks))
final_sequence: List[str] = []

for add in list_of_tasks:
    if add not in task_graph:
        task_graph[add] = []

workers = [Worker() for _ in range(0, number_of_workers)]

current_time = 0
while len(final_sequence) < len(list_of_tasks):
    can_we_start = []
    for task in list_of_tasks:
        dependencies = task_graph.get(task, None)
        if dependencies is not None and len(dependencies) < 1:
            can_we_start.append(task)

    [done(worker.done()) for worker in workers if worker.is_ready(current_time)]

    for task in can_we_start:
        for worker in workers:
            if not worker.is_busy(current_time):
                worker.assign(task, current_time)
                break

    current_time += 1

print(f"{current_time}s")
print("".join(final_sequence))
