import random

class Player():
    def __init__(self, player_number, player_type, mancala):
        self.player_number = player_number
        self.player_type = player_type
        self.mancala = mancala

    def pick_random_pot(self):
        return random.choice(self.mancala.get_legal_moves(self.player_number))

    def play(self):
        if self.player_type == "random":
            pot = self.pick_random_pot()
            return self.mancala.play(self.player_number, pot)



