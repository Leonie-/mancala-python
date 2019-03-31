import csv
import time
import datetime

from mancala_board import MancalaBoard
from game import Game
from player import Player



def generate_game(player_one_type, player_two_type, max_lookahead = 5, time_limit = 5):
    pots = 6
    stones = 4
    first_player = 1

    mancala_board = MancalaBoard(pots, stones, None)
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
        "winner": str(mancala_board.winning_player),
        "final_score_player_1": str(mancala_board.game_board_log[-1][2][0]),
        "final_score_player_2": str(mancala_board.game_board_log[-1][2][1]),
        "final_score_difference": str(abs(
            mancala_board.game_board_log[-1][2][0] - mancala_board.game_board_log[-1][2][1]
        )),
    }
    print(game_outcome)

    return ",".join(game_outcome.values())

def init():
    start_time = datetime.datetime.now()
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

    for player in rounds:
        for index in range(100): # 100 games per combination
            game_outcome = generate_game(player[0], player[1])

            with open('kalah_round_robin.csv', 'a', newline='') as round_robin_csv:
                round_robin_writer = csv.writer(round_robin_csv, delimiter="\t", quoting = csv.QUOTE_NONE)
                round_robin_writer.writerow([game_outcome])

    print(f"Time to run {datetime.datetime.now() - start_time}")

init()
