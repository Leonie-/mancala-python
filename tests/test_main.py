# import unittest.mock as mock
# import mancala.main
#
# class TestInitialisation:
#     @mock.patch('mancala_board.MancalaBoard', wraps = None)
#     @mock.patch('game.Game', wraps = None)
#     @mock.patch('player.Player', wraps = None)
#     @mock.patch('csv.writer', wraps = None)
#     def test_creates_a_new_mancala_board_instance_with_correct_params(self, mancala_board_mock, game_mock, player_mock, csv_writer):
#         mancala.main.init()
#         mancala_board_mock.assert_called_with(6,5)


    # @mock.patch('mancala_board.MancalaBoard', wraps=None, return_value = "game-board")
    # @mock.patch('game.Game', wraps=None)
    # @mock.patch('player.Player', wraps=None, side_effect = ["player1", "player2"])
    # @mock.patch('csv.writer', wraps=None)
    # def test_creates_a_new_game_instance_with_correct_params(self, mancala_board_mock, game_mock, player_mock, csv_writer):
    #     mancala.main.init()
    #     game_mock.assert_called_with("game-board", "player1", "player2")