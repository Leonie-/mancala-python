import unittest.mock as mock

from mancala.game import Game

def test_creates_a_new_game():
    mock_mancala_board = mock.Mock()
    mock_player_one = mock.Mock()
    mock_player_two = mock.Mock()

    game = Game(mock_mancala_board, mock_player_one, mock_player_two)
    assert game.game == mock_mancala_board
    assert game.players == [mock_player_one, mock_player_two]

class TestGamePlay:

    def test_player_one_takes_a_turn(self):
        current_player = 1
        mock_mancala_board = mock.Mock()
        mock_player_one = mock.Mock()
        mock_player_two = mock.Mock()
        mock_mancala_board.game_over.return_value = True
        mock_player_one.play.return_value = False

        game = Game(mock_mancala_board, mock_player_one, mock_player_two)
        game.play(current_player)
        mock_player_one.play.assert_called_once

    def test_player_one_takes_an_extra_turn(self):
        game_over_states = [True, False]
        current_player = 1
        mock_mancala_board = mock.Mock()
        mock_player_one = mock.Mock()
        mock_player_two = mock.Mock()
        mock_mancala_board.game_over.return_value = game_over_states.pop()
        mock_player_one.play.return_value = False

        game = Game(mock_mancala_board, mock_player_one, mock_player_two)
        game.play(current_player)
        mock_player_one.play.assert_called_twice

    def test_returns_the_game_log_on_game_over(self):
        expected_game_log = "[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]]"
        current_player = 1
        mock_mancala_board = mock.Mock()
        mock_player_one = mock.Mock()
        mock_player_two = mock.Mock()
        mock_mancala_board.game_over.return_value = True
        mock_mancala_board.game_log = expected_game_log
        mock_player_one.play.return_value = False

        game = Game(mock_mancala_board, mock_player_one, mock_player_two)
        assert game.play(current_player) == expected_game_log
