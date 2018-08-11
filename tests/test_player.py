import unittest.mock as mock

from mancala.player import Player

def test_creates_a_new_player():
    player = Player(1, "random", mock.Mock())
    assert player.player_number == 1
    assert player.player_type == "random"

class TestRandomPlayer:

    @mock.patch('random.choice', return_value=4)
    def test_creates_a_new_mancala_instance_with_correct_params(self, choice_mock):
        mancala_mock = mock.Mock()
        player = Player(1, "random", mancala_mock)
        player.play()
        mancala_mock.get_legal_moves.assert_called_with(1)

    @mock.patch('random.choice', return_value=4)
    def test_random_player_takes_a_random_move(self, choice_mock):
        mancala_mock = mock.Mock()
        mancala_mock.get_legal_moves.return_value = [1, 6]
        player = Player(1, "random", mancala_mock)
        player.play()
        choice_mock.assert_called_with([1,6])
