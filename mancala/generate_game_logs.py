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

    for game_number in range(5):
        mancala_board = MancalaBoard(pots, stones, None, game_number)
        player_one_type = random.choice(player_types)
        player_two_type = random.choice(player_types)
        max_lookahead = 6
        print(f"player_one_type {player_one_type}, player_two_type {player_two_type}")
        game = Game(
            mancala_board,
            Player(1, player_one_type, mancala_board, max_lookahead),
            Player(2, player_two_type, mancala_board, max_lookahead)
        )
        game_logs = game.play(first_player)
        print(f"game_logs : {game_logs[-1]}")

        with open('kalah_game_board_data.csv', 'a', newline='') as game_board_csv, open('kalah_game_state_data.csv', 'a', newline='') as game_state_csv:
            game_board_writer = csv.writer(game_board_csv)
            game_board_writer.writerow(game_logs[0])

            game_state_writer = csv.writer(game_state_csv)
            game_state_writer.writerow(game_logs[1])

init()
