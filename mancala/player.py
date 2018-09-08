import random

from mancala_board import MancalaBoard

class Player():
    def __init__(self, player_number, player_type, opposite_player_type, mancala, maximum_depth = 4):
        self.player_number = player_number
        self.player_type = player_type
        self.opposite_player_number = self.get_opposite_player(self.player_number)
        self.opposite_player_type = opposite_player_type
        self.mancala = mancala
        self.maximum_depth = maximum_depth

    def get_opposite_player(self, current_player):
        return 2 if current_player == 1 else 1

    def pick_random(self):
        return random.choice(self.mancala.get_legal_moves(self.player_number))

    def minimaxScore(self, game_instance, depth):
        if game_instance.winning_player is self.player_number:
            print(f"Current player wins: {game_instance.game_log[-1]}")
            return 100 - depth
        elif game_instance.winning_player is self.opposite_player_number:
            print(f"Opposite player wins: {game_instance.game_log[-1]}")
            return 0 - depth
        else:
            print(f"Game draw: {game_instance.game_log[-1]}")
            return 50

    def minimaxScoreMidGame(self, game_instance):
        print(f"PLAYER: {self.player_number}")
        player_one_score = game_instance.game_log[-1][2][0]
        player_two_score = game_instance.game_log[-1][2][1]

        player_one_pots = sum(game_instance.game_log[-1][0])
        player_two_pots = sum(game_instance.game_log[-1][0])

        player_one_score += player_one_pots
        player_two_score += player_two_pots

        if player_one_score == player_two_score:
            print(f"Game draw: {game_instance.game_log[-1]}")
            return 50
        elif (player_one_score > player_two_score and self.player_number is 1) or (player_one_score < player_two_score and self.player_number is 2):
            print(f"Current player wins: {game_instance.game_log[-1]}")
            return 100
        else:
            print(f"Opposite player wins: {game_instance.game_log[-1]}")
            return 0

    def minimax(self, game, phasing_player, depth = 0, move = None):
        if game.game_over():
            return [self.minimaxScore(game, depth), move]

        if depth is self.maximum_depth:
            return [self.minimaxScoreMidGame(game), move]

        depth += 1

        scores = []
        moves = []
        legal_moves = game.get_legal_moves(phasing_player)
        last_move = game.game_log[-1]
        next_player = self.get_opposite_player(phasing_player)

        print(f"------Depth {depth} Player {phasing_player} Legal moves: {legal_moves}")

        for move in legal_moves:
            possible_game = MancalaBoard(6, 6, last_move)
            take_another_turn = possible_game.play(phasing_player, move)

            # print(f"Player {phasing_player} moves on pot: {move}")

            if take_another_turn is True:
                next_player = phasing_player

            score = self.minimax(possible_game, next_player, depth, move)[0]
            scores.append(score)
            moves.append(move)

        # Do the min or max calculation
        if phasing_player == self.player_number:
            score_index = scores.index(max(scores))
            return [max(scores), moves[int(score_index)]]
        else:
            score_index = scores.index(min(scores))
            return [min(scores), moves[int(score_index)]]


    def pick_minimax(self):
        phasing_player = self.player_number
        minimax = self.minimax(self.mancala, phasing_player)
        print(f"MINIMAX POT CHOSEN {minimax[1]}")
        return minimax[1]

    def play(self):
        if self.player_type == "random":
            pot = self.pick_random()
            return self.mancala.play(self.player_number, pot)

        if self.player_type == "minimax":
            pot = self.pick_minimax()
            return self.mancala.play(self.player_number, pot)






