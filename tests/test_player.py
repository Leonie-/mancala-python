import unittest.mock as mock

from mancala.player import Player

def test_creates_a_new_player():
    player = Player(1, "random", mock.Mock())
    assert player.player_number == 1
    assert player.player_type == "random"
    assert player.opposite_player_number == 2
    assert player.maximum_depth == 5

class TestRandomPlayer:

    @mock.patch('random.choice', return_value=4)
    def test_creates_a_new_mancala_instance_with_correct_params(self, choice_mock):
        mancala_mock = mock.Mock()
        player = Player(1, "random", mancala_mock)
        player.play()
        mancala_mock.get_legal_moves.assert_called_with(1)

    @mock.patch('random.choice', return_value=6)
    def test_picks_a_random_pot_from_legal_moves_available(self, choice_mock):
        mancala_mock = mock.Mock()
        mancala_mock.get_legal_moves.return_value = [1, 6]
        player = Player(1, "random", mancala_mock)
        player.play()
        choice_mock.assert_called_with([1,6])

    @mock.patch('random.choice', return_value=5)
    def test_move_is_made_in_mancala(self, choice_mock):
        mancala_mock = mock.Mock()
        mancala_mock.get_legal_moves.return_value = [3,4,5,6]
        mancala_mock.play.return_value = True
        player = Player(1, "random", mancala_mock)
        assert player.play() == True
        mancala_mock.play.assert_called_with(1, 5)


# class ScoreMiniMaxScore:
#
#     def test_minimax_scoring_when_current_player_wins(self):
#         mancala_mock = mock.Mock()
#         player = Player(1, "minimax", mancala_mock)
#
#         mancala_mock.get_legal_moves.assert_called_with(1)