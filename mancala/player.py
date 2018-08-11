import random

class Player():
    def __init__(self, player_number, player_type, mancala):
        self.player_number = player_number
        self.player_type = player_type
        self.mancala = mancala

    def play(self):
        if self.player_type == "random":
            return random.choice(self.mancala.get_legal_moves(self.player_number))



