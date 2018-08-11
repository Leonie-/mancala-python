from mancala.mancala import Mancala
import pytest

class TestInitialGameStateDefault:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_returns_game_log(self, mancala):
        assert mancala.game_log == [
            [[4,4,4,4,4,4], [4,4,4,4,4,4], [0,0]]
        ]

class TestInitialGameStateProvided:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4, [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [27, 19]])

    def test_returns_game_log_with_initial_state_when_provided(self, mancala):
        assert mancala.game_log == [
            [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [27, 19]]
        ]

class TestGamePlayValidation:

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

    def test_throws_error_when_the_same_player_takes_too_many_turns(self, mancala):
        mancala.play(1, 2)
        mancala.play(1, 3)

        with pytest.raises(Exception) as error_message:
            mancala.play(1, 4)
        assert str(error_message.value) == "Player cannot take another turn"

class TestGameThrowsWhenEmptyPotIsSelectedForPlay:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4, [[0, 2, 1, 0, 0, 0], [0, 0, 0, 1, 0, 4], [27, 19]])

    def test_game_throws_an_error_when_empty_pot_selected_for_play(self, mancala):
        with pytest.raises(Exception) as error_message:
            mancala.play(1, 1)
        assert str(error_message.value) == "Selected pot must not be empty"

class TestGamePlay:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_increments_player_turn_on_each_play(self, mancala):
        mancala.play(1, 2)
        assert mancala.current_player == 1
        assert mancala.player_turn_number == 1
        mancala.play(1, 6)
        assert mancala.current_player == 1
        assert mancala.player_turn_number == 2
        mancala.play(2, 1)
        assert mancala.current_player == 2
        assert mancala.player_turn_number == 1

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

    def test_game_over_returns_false_if_game_is_not_over(self, mancala):
        mancala.play(1, 1)
        assert mancala.game_over == False

    def test_winning_player_is_none_when_no_one_has_won(self, mancala):
        mancala.play(1, 1)
        assert mancala.winning_player == None

class TestPlayerGetsAnExtraTurn:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 10, [[0, 0, 0, 3, 2, 1], [1, 4, 6, 0, 0, 2], [0, 0]])

    def test_returns_false_when_player_does_not_get_an_extra_turn(self, mancala):
        assert mancala.play(2, 1) == False

    def test_returns_true_when_player_gets_an_extra_turn(self, mancala):
        assert mancala.play(1, 6) == True

    def test_returns_false_when_player_gets_another_extra_turn(self, mancala):
        mancala.play(1, 6)
        assert mancala.play(1, 5) == False


class TestGameEndPlayerOneWin:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4, [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [27, 19]])

    def test_game_over_is_true_and_winning_player_is_set_at_game_end(self, mancala):
        assert mancala.game_over == False
        mancala.play(2, 4)
        assert mancala.game_log[-1] == [[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [27, 20]]
        assert mancala.game_over == True
        assert mancala.winning_player == 1

class TestGameEndPlayerTwoWin:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4, [[0, 0, 0, 0, 5, 0], [1, 0, 0, 0, 0, 0], [20, 20]])

    def test_game_over_is_true_and_winning_player_is_set_at_game_end(self, mancala):
        assert mancala.game_log[-1] == [[0, 0, 0, 0, 5, 0], [1, 0, 0, 0, 0, 0], [20, 20]]
        assert mancala.game_over == False
        mancala.play(2, 1)
        assert mancala.game_log[-1] == [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [20, 26]]
        assert mancala.game_over == True
        assert mancala.winning_player == 2

class TestGameEndDraw:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 10, [[0, 0, 0, 7, 4, 0], [0, 0, 0, 0, 1, 0], [31, 30]])

    def test_game_over_is_true_and_winning_player_is_0_if_draw(self, mancala):
        assert mancala.game_log[0] == [[0, 0, 0, 7, 4, 0], [0, 0, 0, 0, 1, 0], [31, 30]]
        mancala.play(2, 5)
        assert mancala.game_log[1] == [[0, 0, 0, 7, 4, 0], [0, 0, 0, 0, 0, 0], [31, 31]]
        assert mancala.game_over == True
        assert mancala.winning_player == 0

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

class TestExtraTurnWhenLooping:
    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 14)

    def test_returns_true_for_extra_turn_when_looping_around(self, mancala):
        assert mancala.play(1,6) == True

class TestReturnsLegalMoves:
    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(0, 0, [[0, 0, 1, 0, 4, 0], [0, 0, 0, 1, 0, 0], [23, 19]])

    def test_returns_true_for_extra_turn_when_looping_around(self, mancala):
        assert mancala.get_legal_moves(1) == [3, 5]
