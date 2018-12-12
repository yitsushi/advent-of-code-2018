#!/usr/bin/env python3

import advent_of_code as aoc
from typing import List, Dict


def done(_task: str):
    del task_graph[_task]
    final_sequence.append(_task)
    for t in task_graph:
        if task_graph[t] is not None and _task in task_graph[t]:
            task_graph[t].remove(_task)


task_graph: Dict[str, List[str]] = {}
list_of_tasks: List[str] = []

INSTRUCTION_PATTERN = r'^Step (\w) must be finished before step (\w) can begin.$'
(input_file, ) = aoc.parameters()
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


while len(final_sequence) < len(list_of_tasks):
    for task in list_of_tasks:
        dependencies = task_graph.get(task, None)
        if dependencies is not None and len(dependencies) < 1:
            done(task)
            break

print("".join(final_sequence))
