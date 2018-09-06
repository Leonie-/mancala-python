import random

from mancala_board import MancalaBoard

class Player():
    def __init__(self, player_number, player_type, opposite_player_type, mancala):
        self.player_number = player_number
        self.player_type = player_type
        self.opposite_player_number = self.get_opposite_player(self.player_number)
        self.opposite_player_type = opposite_player_type
        self.mancala = mancala

    def get_opposite_player(self, current_player):
        return 2 if current_player == 1 else 1

    def pick_random(self):
        return random.choice(self.mancala.get_legal_moves(self.player_number))

    def minimaxScore(self, game_instance, depth):
        if game_instance.winning_player is self.player_number:
            print(f"Current player wins: {game_instance.game_log[-1]}")
            return 10
        elif game_instance.winning_player is self.opposite_player_number:
            print(f"Opposite player wins: {game_instance.game_log[-1]}")
            return -10
        else:
            print(f"Game draw: {game_instance.game_log[-1]}")
            return 0

    def minimax(self, game, phasing_player, depth = 0):
        if game.game_over():
            return self.minimaxScore(game, depth)

        depth += 1

        # if depth > 8:
        #     return 10

        scores = []
        moves = []
        legal_moves = game.get_legal_moves(phasing_player)
        last_move = game.game_log[-1]
        next_player = self.get_opposite_player(phasing_player)

        print(f"------Depth {depth} Player {phasing_player} Legal moves: {legal_moves}")

        for move in legal_moves:
            possible_game = MancalaBoard(3, 3, last_move)
            take_another_turn = possible_game.play(phasing_player, move)

            print(f"Move on pot: {move}")

            if take_another_turn is True:
                next_player = phasing_player

            score = self.minimax(possible_game, next_player, depth)
            scores.append(score)
            moves.append(move)

        # Do the min or max calculation
        if phasing_player == self.player_number:
            return scores.index(max(scores))
        else:
            return scores.index(min(scores))


    def pick_minimax(self):
        phasing_player = self.player_number
        return self.minimax(self.mancala, phasing_player)


    def play(self):
        if self.player_type == "random":
            pot = self.pick_random()
            return self.mancala.play(self.player_number, pot)

        if self.player_type == "minimax":
            pot = self.pick_minimax()
            return self.mancala.play(self.player_number, pot)






