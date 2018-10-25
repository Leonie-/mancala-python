import random

from mancala_board import MancalaBoard

class Player():
    def __init__(self, player_number, player_type, mancala, maximum_depth = float("inf")):
        self.player_number = player_number
        self.player_type = player_type
        self.opposite_player_number = self.get_opposite_player(self.player_number)
        self.mancala = mancala
        self.maximum_depth = maximum_depth

    def get_opposite_player(self, current_player):
        return 2 if current_player == 1 else 1

    def pick_random(self):
        return random.choice(self.mancala.get_legal_moves(self.player_number))

    def calculate_winner(self, board_state):
        player_one_score = board_state[2][0] + sum(board_state[0])
        player_two_score = board_state[2][1] + sum(board_state[1])

        if player_one_score > player_two_score:
            return 1
        elif player_one_score < player_two_score:
            return 2
        else:
            return 0

    def minimaxScore(self, game_instance, depth, game_over):
        last_move = game_instance.game_log[-1]
        winner = game_instance.winning_player if game_over else self.calculate_winner(last_move)

        if winner is self.player_number:
            # print(f"Current player wins: {game_instance.game_log[-1]}")
            return 100 - depth
        elif winner is self.opposite_player_number:
            # print(f"Opposite player wins: {game_instance.game_log[-1]}")
            return 0 - depth
        else:
            # print(f"Game draw: {game_instance.game_log[-1]}")
            return 50

    def minimax(self, game, phasing_player, depth = 0, move = None):
        game_over = game.game_over()
        if game_over or depth is self.maximum_depth:
            return [self.minimaxScore(game, depth, game_over), move]

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

    def minimax_alpha_beta_score(self, game_instance, depth, game_over):
        last_move = game_instance.game_log[-1]
        scores = last_move[2]
        winner = game_instance.winning_player if game_over else self.calculate_winner(last_move)

        if winner is self.player_number or winner is self.opposite_player_number:
            print(f"Final board: {game_instance.game_log[-1]}, scores {scores}")
            return scores[self.player_number - 1] - scores[self.opposite_player_number - 1] - depth
        else:
            print(f"Game draw: {game_instance.game_log[-1]}")
            return 0

    def minimax_alpha_beta(self, game, phasing_player, alpha = float("-inf"), beta = float("inf"), best_move = None, depth = -1):
        game_over = game.game_over()
        if game_over:
            return [self.minimax_alpha_beta_score(game, depth, game_over), best_move]
        elif depth is self.maximum_depth:
            game.clear_board()
            return [self.minimax_alpha_beta_score(game, depth, game_over), best_move]

        depth += 1

        legal_moves = game.get_legal_moves(phasing_player)
        last_move = game.game_log[-1]
        next_player = self.get_opposite_player(phasing_player)

        print(f"------Depth {depth} Player {phasing_player} Legal moves: {legal_moves}")

        for index, move in enumerate(legal_moves, start=0):
            possible_game = MancalaBoard(6, 6, last_move)
            take_another_turn = possible_game.play(phasing_player, move)
            # See what the next player will do
            if phasing_player == self.player_number: #is maximising node
                result = self.minimax_alpha_beta(possible_game, next_player, alpha, beta, move, depth)[0]
                if result > alpha:
                    print(f" Max best move: {best_move} - result {result} is more than {alpha}, set alpha to {result}")
                    alpha = result
                    best_move = move

                if alpha >= beta: # Pruning
                    break

            else: #is minimising node
                result = self.minimax_alpha_beta(possible_game, next_player, alpha, beta, move, depth)[0]
                if result < beta:
                    print(f" Min best move: {best_move} - result {result} is less than {beta}, set beta to {result}")
                    beta = result
                    best_move = move

                if beta <= alpha:  # Pruning
                    break

        best_score = alpha if phasing_player == self.player_number else beta
        return [best_score, best_move]


    def pick_minimax_alpha_beta(self):
        return self.minimax_alpha_beta(self.mancala, self.player_number)[1]

    def pick_minimax(self):
        return self.minimax(self.mancala, self.player_number)[1]

    def pick_right_pot(self):
         return self.mancala.get_legal_moves(self.player_number)[-1]

    def pick_pot_with_most_stones(self):
        last_move_for_player = self.mancala.game_log[-1][self.player_number - 1]
        max_stones = max(last_move_for_player)
        return last_move_for_player.index(max_stones)

    def pick_pot_with_least_stones(self):
        last_move_for_player = self.mancala.game_log[-1][self.player_number - 1]
        return min(i for i in last_move_for_player if i > 0)

    def play(self):
        pot = self.pick_random()

        if self.player_type == "minimax":
            pot = self.pick_minimax()

        if self.player_type == "alphabeta":
            pot = self.pick_minimax_alpha_beta()

        if self.player_type == "rightpot":
            pot = self.pick_right_pot()

        if self.player_type == "potwithleast":
            pot = self.pick_pot_with_least_stones()

        if self.player_type == "potwithmost":
            pot = self.pick_pot_with_most_stones()

        print(f"Pot chosen for play: {pot}")

        return self.mancala.play(self.player_number, pot)






