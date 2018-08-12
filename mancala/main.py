import csv

from mancala_board import MancalaBoard
from player import Player

class Game():
    def __init__(self):
        self.game = MancalaBoard(6, 4)
        self.players = [
            Player(1, "random", self.game),
            Player(2, "random", self.game)
        ]

    def switch_players(self, current_player):
        return 1 if current_player is 2 else 2

    def play(self, current_player):
        take_turn = self.players[current_player - 1].play()

        if self.game.game_over is True:
            # print("Game Over")
            return self.game.game_log

        if take_turn == True:
            # Player takes an extra turn
            # print("Extra Turn for player {current_player}")
            self.players[current_player - 1].play()

        # Switch players and continue
        opposite_player = self.switch_players(current_player)
        # print(f"Switched to player {opposite_player}")
        return self.play(opposite_player)

game = Game()
game_log = game.play(1)

with open('mancala_game_data.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(game_log)
