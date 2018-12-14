from advent_of_code import BaseSolution
from typing import List, Dict
from .worker import Worker


class Solution(BaseSolution):
    task_graph: Dict[str, List[str]] = {}
    list_of_tasks: List[str] = []
    final_sequence: List[str] = []
    workers: List[Worker]

    def setup(self):
        self.task_graph = {}
        self.list_of_tasks = []
        self.final_sequence = []

        instruction_pattern = r'^Step (\w) must be finished before step (\w) can begin.$'
        (input_file, ) = self.parameters()
        for line in self.read_input(input_file):
            task1, task2 = self.parse(line, instruction_pattern, (str, str))
            self.task_graph[task2] = self.task_graph.get(task2, []) + [task1]
            self.list_of_tasks.extend((task1, task2))

        self.list_of_tasks = sorted(set(self.list_of_tasks))

        for add in self.list_of_tasks:
            if add not in self.task_graph:
                self.task_graph[add] = []

    def done_task(self, _task: str):
        if _task in self.task_graph:
            # For part1
            del self.task_graph[_task]

        self.final_sequence.append(_task)
        for t in self.task_graph:
            if self.task_graph[t] is not None and _task in self.task_graph[t]:
                self.task_graph[t].remove(_task)

    def loop(self) -> int:
        current_time = 0
        while len(self.final_sequence) < len(self.list_of_tasks):
            can_we_start = []
            for task in self.list_of_tasks:
                dependencies = self.task_graph.get(task, None)
                if dependencies is not None and len(dependencies) < 1:
                    can_we_start.append(task)

            [self.done_task(w.done()) for w in self.workers if w.is_ready(current_time)]

            for task in can_we_start:
                for w in self.workers:
                    if not w.is_busy(current_time):
                        del self.task_graph[task]
                        w.assign(task, current_time)
                        break

            current_time += 1

        return current_time

    def part1(self) -> str:
        self.workers = [Worker(1)]
        self.loop()
        return "".join(self.final_sequence)

    def part2(self) -> int:
        self.workers = [Worker(60) for _ in range(0, 5)]
        time_elapsed = self.loop()
        return time_elapsed
