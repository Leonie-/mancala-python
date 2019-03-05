import csv
import time

from mancala_board import MancalaBoard
from game import Game
from player import Player



def generate_game(game_number, player_one_type, player_two_type, max_lookahead = 2, time_limit = 2):
    pots = 6
    stones = 4
    first_player = 1

    mancala_board = MancalaBoard(pots, stones, None, game_number)
    print(f"game number [game_number] player_one_type [player_one_type], player_two_type [player_two_type]")
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
        "final_score_difference": abs(
            mancala_board.game_board_log[-1][2][0] - mancala_board.game_board_log[-1][2][1]),
    }
    print(game_outcome)

    return game_outcome

def init():
    start = time.time()
    game_number = 0
    rounds = [["mcts", "mcts-expansion-gsp"],
        ["mcts", "mcts-expansion-apriori"],
        ["mcts", "mcts-expansion-minimax"],
        ["mcts-expansion-gsp", "mcts"],
        ["mcts-expansion-gsp", "mcts-expansion-apriori"],
        ["mcts-expansion-gsp", "mcts-expansion-minimax"],
        ["mcts-expansion-apriori", "mcts"],
        ["mcts-expansion-apriori", "mcts-expansion-gsp"],
        ["mcts-expansion-apriori", "mcts-expansion-minimax"],
        ["mcts-expansion-minimax", "mcts"],
        ["mcts-expansion-minimax", "mcts-expansion-gsp"],
        ["mcts-expansion-minimax", "mcts-expansion-apriori"]]

    for round in rounds:
        for index in range(1): # 5 games per combination
            game_number += 1
            game_outcome = generate_game(game_number, round[0], round[1])

            with open('kalah_round_robin.csv', 'a', newline='') as round_robin_csv:
                round_robin_writer = csv.writer(round_robin_csv)
                round_robin_writer.writerow([game_outcome])

    end = time.time()
    print(f"Time to run {end - start})

init()
