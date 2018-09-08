import csv

from mancala_board import MancalaBoard
from game import Game
from player import Player

def init():
    mancala_board = MancalaBoard(6,4)
    player_one_type = "random"
    player_two_type = "random"
    game = Game(
        mancala_board,
        Player(1, player_one_type, mancala_board),
        Player(2, player_two_type, mancala_board)
    )
    first_player = 1
    game_log = game.play(first_player)

    with open('mancala_game_data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(game_log)

init()
