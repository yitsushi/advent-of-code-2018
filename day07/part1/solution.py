#!/usr/bin/env python3

import advent_of_code as aoc

def done(task):
    task_graph[task] = None
    final_sequence.append(task)
    for t in task_graph:
        if task_graph[t] is not None and task in task_graph[t]:
            task_graph[t].remove(task)

task_graph = {}
list_of_tasks = []

INSTRUCTION_PATTERN = r'^Step (\w) must be finished before step (\w) can begin.$'
input_file = aoc.parameters(1, (str, ))
for line in aoc.read_input(input_file):
    task1, task2 = aoc.parse(line, INSTRUCTION_PATTERN, (str, str))
    task_graph[task2] = task_graph.get(task2, []) + [task1]
    list_of_tasks.append(task1)
    list_of_tasks.append(task2)

list_of_tasks = sorted(set(list_of_tasks))
final_sequence = []

for add in list_of_tasks:
    if add not in task_graph:
        task_graph[add] = []


while len(final_sequence) < len(list_of_tasks):
    for task in list_of_tasks:
        deps = task_graph.get(task, None)
        if deps is not None and len(deps) < 1:
            done(task)
            break

print("".join(final_sequence))
