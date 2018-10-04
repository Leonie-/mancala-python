class Game():
    def __init__(self, mancala_board, player_one, player_two):
        self.game = mancala_board
        self.players = [player_one, player_two]

    def switch_players(self, current_player):
        return 1 if current_player is 2 else 2

    def play(self, current_player):
        player = self.players[current_player - 1]
        take_turn = player.play()

        if self.game.game_over() is True:
            return self.game.game_log

        if take_turn is True:
            # Player takes an extra turn
            player.play()
            if self.game.game_over() is True:
                return self.game.game_log

        # Switch players and continue
        opposite_player = self.switch_players(current_player)

        return self.play(opposite_player)