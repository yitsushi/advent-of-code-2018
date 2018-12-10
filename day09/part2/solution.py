#!/usr/bin/env python3

import operator, os, logging
from logging.config import dictConfig
from collections import deque

_logLevel = os.getenv('LOG_LEVEL', None)

if _logLevel == 'debug':
    logLevel = logging.DEBUG
elif _logLevel == 'info':
    logLevel = logging.INFO
else:
    logLevel = logging.ERROR


logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logLevel}
        },
    root = {
        'handlers': ['h'],
        'level': logLevel,
        },
)
dictConfig(logging_config)
Log = logging.getLogger()

class Configuration:
    NumberOfPlayers = 10
    LastMarble = 1618

    def __init__(self, last_marble, number_of_players):
        if last_marble is not None:
            self.LastMarble = last_marble
        if number_of_players is not None:
            self.NumberOfPlayers = number_of_players

class ScoreBoard:
    players = None

    def __init__(self):
        self.players = {}

    def add_score(self, player, score):
        self.players[player] = self.players.get(player, 0) + score

    def winner(self):
        max(self.players.iteritems(), key=operator.itemgetter(1))[0]

    def high_score(self):
        return max(self.players.values())

class Circle:
    config = None
    scoreBoard = None
    marbles = None
    currentPlayer = 0
    marbleInHand = 0
    percentProgress = 0

    def __init__(self, *, number_of_players=None, last_marble=None):
        self.scoreBoard = ScoreBoard()
        self.config = Configuration(last_marble, number_of_players)
        self.marbles = deque()
        self.marbles.append(0)
        self.marbleInHand = 1
        self.percentProgress = int(last_marble / 100)
        Log.info("Rounds per Percent: {:d}".format(self.percentProgress))

    def is_it_over_yet(self):
        return self.marbleInHand > self.config.LastMarble

    def put(self):
        if self.marbleInHand % self.percentProgress == 0:
            Log.info(
                    'Player #%d puts down marble #%d (%d%%)',
                    self.currentPlayer, self.marbleInHand,
                    self.marbleInHand / self.percentProgress)

        if self.marbleInHand % 23 == 0:
            self.marbles.rotate(7)
            self.scoreBoard.add_score(self.currentPlayer, self.marbles.pop() + self.marbleInHand)
            self.marbles.rotate(-1)
        else:
            self.marbles.rotate(-1)
            self.marbles.append(self.marbleInHand)

        Log.debug('Board looks like: %s', self.marbles)

        self.marbleInHand += 1
        self.currentPlayer = (self.currentPlayer + 1) % self.config.NumberOfPlayers

    def winner(self):
        return self.scoreBoard.winner()

    def high_score(self):
        return self.scoreBoard.high_score()

area = Circle(number_of_players=424, last_marble=71482*100)

while not area.is_it_over_yet():
    area.put()

print(area.high_score())
