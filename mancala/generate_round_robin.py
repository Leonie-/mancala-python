import csv
import random

from mancala_board import MancalaBoard
from game import Game
from player import Player


def init():
    pots = 6
    stones = 4
    first_player = 1
    # player_types = ["minimax", "alphabeta", "random", "rightpot", "leftpot", "potwithfewest", "potwithmost", "takeanotherturn", "avoidanotherturn", "mcts"]
    player_types = ["mcts"]
    # player_types = ["mcts-expansion-no-extra-turn"]
    # player_types = ["mcts_simulation_minimax"]

    for game_number in range(2):
        mancala_board = MancalaBoard(pots, stones, None, game_number)
        player_one_type = random.choice(player_types)
        player_two_type = random.choice(player_types)
        max_lookahead = 2
        time_limit = 2  # Used for MCTS simulations only
        print(f"player_one_type {player_one_type}, player_two_type {player_two_type}")
        game = Game(
            mancala_board,
            Player(1, player_one_type, mancala_board, max_lookahead, time_limit),
            Player(2, player_two_type, mancala_board, max_lookahead, time_limit)
        )
        game.play(first_player)
        game_outcome = {
            "player_one": player_one_type,
            "player_two": player_two_type,
            "winner": mancala_board.winning_player,
            "final_score_player_1": mancala_board.game_board_log[-1][2][0],
            "final_score_player_2": mancala_board.game_board_log[-1][2][1],
            "final_score_difference": abs(mancala_board.game_board_log[-1][2][0] - mancala_board.game_board_log[-1][2][1]),
        }
        print(game_outcome)

        with open('kalah_round_robin.csv', 'a', newline='') as round_robin_csv:
            round_robin_writer = csv.writer(round_robin_csv)
            round_robin_writer.writerow([game_outcome])

init()
