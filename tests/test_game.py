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
        assert mock_player_one.play.call_count == 1

    def test_player_one_takes_an_extra_turn(self):
        current_player = 1
        mock_mancala_board = mock.Mock()
        mock_player_one = mock.Mock()
        mock_player_two = mock.Mock()
        mock_mancala_board.game_over.side_effect = [False, True]
        mock_player_one.play.side_effect = [True, False]

        game = Game(mock_mancala_board, mock_player_one, mock_player_two)
        game.play(current_player)

        assert mock_player_one.play.call_count == 2

    def test_player_two_takes_a_turn_after_player_one(self):
        current_player = 1
        mock_mancala_board = mock.Mock()
        mock_player_one = mock.Mock()
        mock_player_two = mock.Mock()
        mock_mancala_board.game_over.side_effect = [False, False, True]
        mock_player_one.play.side_effect = [False, False]
        mock_player_two.play.side_effect = [False]

        game = Game(mock_mancala_board, mock_player_one, mock_player_two)
        game.play(current_player)

        assert mock_player_one.play.call_count == 2
        assert mock_player_two.play.call_count == 1

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

    def test_does_not_switch_players_when_game_over_occurs_on_a_players_extra_turn(self):
        expected_game_log = "[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [23, 19]]"
        current_player = 1
        mock_mancala_board = mock.Mock()
        mock_player_one = mock.Mock()
        mock_player_two = mock.Mock()
        mock_mancala_board.game_log = expected_game_log
        mock_mancala_board.game_over.side_effect = [False, True]
        mock_player_one.play.side_effect = [True, False]

        game = Game(mock_mancala_board, mock_player_one, mock_player_two)
        game.play(current_player)
        assert not mock_player_two.play.called
