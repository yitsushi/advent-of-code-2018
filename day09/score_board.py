from typing import Dict


class ScoreBoard:
    players: Dict[int, int]

    def __init__(self):
        self.players = {}

    def add_score(self, player: int, score: int):
        self.players[player] = self.players.get(player, 0) + score

    def high_score(self) -> int:
        return max(self.players.values())
