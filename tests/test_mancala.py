from mancala.mancala import Mancala
import pytest

class TestMancalaInit:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_has_starting_number_of_pots(self, mancala):
        assert mancala.number_of_pots == 6

    def test_has_starting_number_of_stones(self, mancala):
        assert mancala.number_of_stones == 4

    def test_has_starting_stores(self, mancala):
        assert mancala.stores == [0,0]

    def test_has_player_1_pots(self, mancala):
        assert mancala.player1 == [4,4,4,4,4,4]

    def test_has_player_2_pots(self, mancala):
        assert mancala.player2 == [4,4,4,4,4,4]


class TestGameState:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_returns_game_state(self, mancala):
        assert mancala.gameState == [
            [[4,4,4,4,4,4], [4,4,4,4,4,4], [0,0]]
        ]
