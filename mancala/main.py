import csv

from mancala_board import MancalaBoard
from game import Game
from player import Player

mancala_board = MancalaBoard(6,4)
game = Game(
    mancala_board,
    Player(1, "random", mancala_board),
    Player(2, "random", mancala_board)
)
first_player = 1
game_log = game.play(first_player)

with open('mancala_game_data.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(game_log)
