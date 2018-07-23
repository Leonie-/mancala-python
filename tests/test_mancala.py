from mancala.mancala import Mancala
import pytest

class TestInitialGameState:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_returns_initial_game_log(self, mancala):
        assert mancala.game_log == [
            [[4,4,4,4,4,4], [4,4,4,4,4,4], [0,0]]
        ]

class TestGamePlay:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_throws_error_when_player_number_is_too_high(self, mancala):
        player_number = 3
        pot_number = 4

        with pytest.raises(ValueError) as error_message:
            mancala.play(player_number, pot_number)
        assert str(error_message.value) == "A valid player must be given"

    def test_throws_error_when_player_number_is_too_low(self, mancala):
        player_number = 0
        pot_number = 2

        with pytest.raises(ValueError) as error_message:
            mancala.play(player_number, pot_number)
        assert str(error_message.value) == "A valid player must be given"

    def test_throws_error_when_pot_selected_does_not_exist(self, mancala):
        player_number = 1
        pot_number = 7

        with pytest.raises(Exception) as error_message:
            mancala.play(player_number, pot_number)
        assert str(error_message.value) == "A valid pot must be selected for play"

    def test_updates_game_log_when_player_one_has_taken_a_move_on_pot_3(self, mancala):
        player_number = 1
        pot_number = 3
        mancala.play(player_number, pot_number)

        assert mancala.game_log[0] == [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]]
        assert mancala.game_log[1] == [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]]

    def test_updates_game_log_when_player_two_has_taken_a_move_on_pot_4(self, mancala):
        player_number = 2
        pot_number = 4
        mancala.play(player_number, pot_number)

        assert mancala.game_log[0] == [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]]
        assert mancala.game_log[1] == [[5, 4, 4, 4, 4, 4], [4, 4, 4, 0, 5, 5], [0, 1]]
