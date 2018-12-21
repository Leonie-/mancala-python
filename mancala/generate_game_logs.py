import csv
import random

from mancala_board import MancalaBoard
from game import Game
from player import Player


def init():
    pots = 6
    stones = 4
    first_player = 1
    player_types = ["minimax", "alphabeta", "random", "rightpot", "potwithleast", "potwithmost", "takeanotherturn", "avoidanotherturn"]

    for lp in range(5000):
        print(f"ITERATION {lp}")
        mancala_board = MancalaBoard(pots, stones)
        player_one_type = random.choice(player_types)
        player_two_type = random.choice(player_types)
        max_lookahead = 6
        print(f"player_one_type {player_one_type}, player_two_type {player_two_type}")
        game = Game(
            mancala_board,
            Player(1, player_one_type, mancala_board, max_lookahead),
            Player(2, player_two_type, mancala_board, max_lookahead)
        )
        game_log = game.play(first_player)

        with open('mancala_game_data.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow(game_log)


init()
