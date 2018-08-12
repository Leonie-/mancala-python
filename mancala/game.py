class Game():
    def __init__(self, mancala_board, player_one, player_two):
        self.game = mancala_board
        self.players = [player_one, player_two]

    def switch_players(self, current_player):
        return 1 if current_player is 2 else 2

    def play(self, current_player):
        take_turn = self.players[current_player - 1].play()
        print(f"GAME OVER: {self.game.game_over()}")
        game_over = self.game.game_over()
        if game_over is True:
            return self.game.game_log

        if take_turn == True:
            # Player takes an extra turn
            print("Extra Turn for player {current_player}")
            self.players[current_player - 1].play()

        # Switch players and continue
        opposite_player = self.switch_players(current_player)
        # print(f"Switched to player {opposite_player}")
        return self.play(opposite_player)