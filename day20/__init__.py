from advent_of_code import BaseSolution
import networkx as nx
import matplotlib.pyplot as plt


class Solution(BaseSolution):
    building: nx.Graph

    def setup(self):
        (input_file, ) = self.parameters()
        pattern: str = list(self.read_input(input_file))[0][1:-1]
        # print(pattern)
        self.building = nx.Graph()

        # First time to use f* complex number.
        # Why the hell I managed Vector2D's all the time :/
        # Ok because it's easier to read later, but still.
        direction_map = {
            'N': 1,
            'E': 1j,
            'S': -1,
            'W': -1j
        }

        position = {0}
        start_set = {0}
        end_set = set()
        possibilities = []

        for ch in pattern:
            if ch == '|':
                # alternative path is coming
                end_set.update(position)
                position = start_set
            elif ch in 'NESW':
                # just go and build the graph
                direction = direction_map[ch]
                self.building.add_edges_from((pos, pos+direction) for pos in position)
                position = {pos + direction for pos in position}
            elif ch == '(':
                # new group
                possibilities.append((start_set, end_set))
                start_set = position
                end_set = set()
            elif ch == ')':
                # end of group
                position.update(end_set)
                start_set, end_set = possibilities.pop()
            else:
                raise Exception(f'Unrecognized character {ch}')

    def draw(self):
        # Ahahah my computer said not enough memory to draw my real input XD
        # But fancy with example ones
        pos = nx.spring_layout(self.building)
        nx.draw_networkx(self.building, pos, with_labels=False)
        node_labels = nx.get_node_attributes(self.building, 'alias')
        nx.draw_networkx_labels(self.building, pos, node_labels)
        plt.show()

    def part1(self):
        all_distances = nx.algorithms.shortest_path_length(self.building, 0)
        return max(all_distances.values())

    def part2(self):
        all_distances = nx.algorithms.shortest_path_length(self.building, 0)
        # Fuuuuuuuuuu
        # At least means '>= 1000' and not '> 1000'
        return len([d for d in all_distances.values() if d >= 1000])
