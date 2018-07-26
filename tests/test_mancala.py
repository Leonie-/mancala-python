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

    def test_returns_false_when_player_does_not_get_another_turn(self, mancala):
        player_number = 1
        pot_number = 2
        assert mancala.play(player_number, pot_number) == False

    def test_returns_true_when_player_gets_another_turn(self, mancala):
        player_number = 1
        pot_number = 3
        assert mancala.play(player_number, pot_number) == True

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

    def test_updates_game_log_when_a_turn_loops_around_to_the_other_side_of_the_board(self, mancala):
        player_number = 1
        pot_number = 6
        mancala.play(player_number, pot_number)

        assert mancala.game_log[0] == [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]]
        assert mancala.game_log[1] == [[4, 4, 4, 4, 4, 0], [5, 5, 5, 4, 4, 4], [1, 0]]

    def test_updates_game_log_with_opposite_capture_when_a_turn_ends_in_the_current_players_empty_pot(self, mancala):
        mancala.play(1, 6)
        mancala.play(2, 2)
        mancala.play(1, 2)

        assert mancala.game_log[0] == [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]]
        assert mancala.game_log[1] == [[4, 4, 4, 4, 4, 0], [5, 5, 5, 4, 4, 4], [1, 0]]
        assert mancala.game_log[2] == [[4, 4, 4, 4, 4, 0], [5, 0, 6, 5, 5, 5], [1, 1]]
        assert mancala.game_log[3] == [[4, 0, 5, 5, 5, 0], [0, 0, 6, 5, 5, 5], [7, 1]]

class TestGamePlayWithLooping:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 10)

    def test_updates_game_log_when_a_turn_loops_around_and_does_not_sow_in_opponents_store(self, mancala):
        player_number = 1
        pot_number = 5
        mancala.play(player_number, pot_number)

        assert mancala.game_log[0] == [[10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10], [0, 0]]
        assert mancala.game_log[1] == [[11, 11, 10, 10, 0, 11], [11, 11, 11, 11, 11, 11], [1, 0]]

