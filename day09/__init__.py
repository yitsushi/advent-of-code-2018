from advent_of_code import BaseSolution
from .playground import Playground


class Solution(BaseSolution):
    game: Playground

    def setup(self):
        _nop, _lm = self.parameters((int, int), ('Number of Players', 'Value of The Last Marble'), (424, 71482))
        self.game = Playground(number_of_players=_nop, last_marble=_lm)

    def play(self):
        while not self.game.is_it_over_yet():
            self.game.put_marble()

    def part1(self):
        self.play()

        return self.game.high_score()

    def part2(self):
        self.game.set_last_marble(self.game.config.last_marble * 100)
        self.play()

        return self.game.high_score()
