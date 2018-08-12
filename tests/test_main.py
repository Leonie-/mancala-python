import unittest.mock as mock

from mancala.mancala_board import MancalaBoard
# from mancala.main import *
#
# def test_sets_first_player_number():
#     assert game.current_player == 1
#
# class TestInitialisation:
#     @mock.patch('Mancala.__init__')
#     def test_creates_a_new_mancala_instance_with_correct_params(self, mancala_mock):
#         game = Game()
#         mancala_mock.assert_called_with(6,5)
#
#     @mock.patch('random.choice', return_value=6)
#     def test_picks_a_random_pot_from_legal_moves_available(self, choice_mock):
#         mancala_mock = mock.Mock()
#         mancala_mock.get_legal_moves.return_value = [1, 6]
#         player = Player(1, "random", mancala_mock)
#         player.play()
#         choice_mock.assert_called_with([1,6])
#
#     @mock.patch('random.choice', return_value=5)
#     def test_move_is_made_in_mancala(self, choice_mock):
#         mancala_mock = mock.Mock()
#         mancala_mock.get_legal_moves.return_value = [3,4,5,6]
#         mancala_mock.play.return_value = True
#         player = Player(1, "random", mancala_mock)
#         assert player.play() == True
#         mancala_mock.play.assert_called_with(1, 5)
