import csv
import random

from mancala_board import MancalaBoard
from game import Game
from player import Player


def init():
    pots = 6
    stones = 4
    first_player = 1
    player_types = ["random", "rightpot"]
    # player_types = ["random", "rightpot", "minimax", "alphabeta"]

    for lp in range(10):
        mancala_board = MancalaBoard(pots, stones)
        player_one_type = random.choice(player_types)
        player_two_type = random.choice(player_types)
        game = Game(
            mancala_board,
            Player(1, player_one_type, mancala_board),
            Player(2, player_two_type, mancala_board)
        )
        game_log = game.play(first_player)

        with open('mancala_game_data.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow(game_log)


init()
