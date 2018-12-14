from collections import deque
from .configuration import Configuration
from .score_board import ScoreBoard


class Playground:
    config = None
    score_board = None
    marbles = None
    current_player = 0
    marble_in_hand = 0

    def __init__(self, *, number_of_players=None, last_marble=None):
        self.score_board = ScoreBoard()
        self.config = Configuration(last_marble, number_of_players)
        self.marbles = deque()
        self.marbles.append(0)
        self.marble_in_hand = 1

    def set_last_marble(self, value: int):
        self.config.last_marble = value

    def is_it_over_yet(self) -> bool:
        return self.marble_in_hand > self.config.last_marble

    def put_marble(self):
        if self.marble_in_hand % 23 == 0:
            self.marbles.rotate(7)
            self.score_board.add_score(self.current_player, self.marbles.pop() + self.marble_in_hand)
            self.marbles.rotate(-1)
        else:
            self.marbles.rotate(-1)
            self.marbles.append(self.marble_in_hand)

        self.marble_in_hand += 1
        self.current_player = (self.current_player + 1) % self.config.number_of_players

    def high_score(self) -> int:
        return self.score_board.high_score()
