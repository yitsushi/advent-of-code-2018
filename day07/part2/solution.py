#!/usr/bin/env python3

import advent_of_code as aoc

class Worker:
    item = None
    busy_until = -1

    def is_busy(self, time):
        return time <= self.busy_until

    def is_ready(self, time):
        return self.item is not None and time >= self.busy_until

    def done(self):
        print(f'Task "{self.item}" is done [{id(self)}]')
        task = self.item
        self.item = None
        return task

    def assign(self, task, current_time):
        task_graph[task] = None
        self.item = task
        self.busy_until = current_time + task_default_length + (ord(task) - 64) - 1
        print(f'Task "{task}" assigned to {id(self)} -> {self.busy_until}')

def done(task):
    final_sequence.append(task)
    for t in task_graph:
        if task_graph[t] is not None and task in task_graph[t]:
            task_graph[t].remove(task)

task_graph = {}
list_of_tasks = []

INSTRUCTION_PATTERN = r'^Step (\w) must be finished before step (\w) can begin.$'
input_file, number_of_workers, task_default_length = aoc.parameters(
        (str, int, int),
        ('Input File', 'NUmber of Workers', 'Default Task Length')
        (None, 5, 60))
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

workers = [Worker() for _ in range(0, number_of_workers)]

current_time = 0
while len(final_sequence) < len(list_of_tasks):
    #print(f'>>> {current_time}s   -> {final_sequence}')

    can_we_start = []
    for task in list_of_tasks:
        deps = task_graph.get(task, None)
        if deps is not None and len(deps) < 1:
            can_we_start.append(task)

    [done(worker.done()) for worker in workers if worker.is_ready(current_time)]

    #can_we_start.sort()
    #print(current_time, can_we_start)

    for task in can_we_start:
        for worker in workers:
            if not worker.is_busy(current_time):
                worker.assign(task, current_time)
                break

    current_time += 1

print(f"{current_time}s")
print("".join(final_sequence))

"""
 +++ [A] ['C']
 +++ [B] ['A']
                 +++ [C] []
 +++ [D] ['A']
 +++ [E] ['B', 'D', 'F']
 +++ [F] ['C']

0: C(3)
1: C(2)
2: C(1)
3: A(1)  F(6)       C
4: B(2)  F(5)       CA
5: B(1)  F(4)       CA
6: D(4)  F(3)       CAB
7: D(3)  F(2)
8: D(2)  F(1)       CABF
9: D(1)  E(5)       CABFD
"""
