import unittest.mock as mock

from mancala.player import Player

def test_creates_a_new_player():
    mancala_mock = mock.Mock()
    player = Player(1, "random", mancala_mock)
    assert player.player_number == 1
    assert player.player_type == "random"


def test_creates_a_new_mancala_instance_with_correct_params():
    mancala_mock = mock.Mock()
    player = Player(1, "random", mancala_mock)
    player.play()
    mancala_mock.get_legal_moves.assert_called_with(1)

@mock.patch('random.choice')
def test_random_player_takes_a_random_move(self, choice_mock):
    choice_mock.return_value = 4
    mancala_mock = mock.Mock()
    player = Player(1, "random", mancala_mock)
    assert player.play() == 4