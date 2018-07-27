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

    def test_game_over_returns_false_if_game_is_not_over(self, mancala):
        mancala.play(1, 1)
        assert mancala.game_over == False

    def test_game_over_returns_true_if_game_is_over(self, mancala):
        assert mancala.game_log[-1] == [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[4, 4, 4, 4, 4, 0], [5, 5, 5, 4, 4, 4], [1, 0]]
        mancala.play(2, 2)
        assert mancala.game_log[-1] == [[4, 4, 4, 4, 4, 0], [5, 0, 6, 5, 5, 5], [1, 1]]
        mancala.play(1, 2)
        assert mancala.game_log[-1] == [[4, 0, 5, 5, 5, 0], [0, 0, 6, 5, 5, 5], [7, 1]]
        mancala.play(2, 6)
        assert mancala.game_log[-1] == [[5, 1, 6, 6, 5, 0], [0, 0, 6, 5, 5, 0], [7, 2]]
        mancala.play(1, 5)
        assert mancala.game_log[-1] == [[5, 1, 6, 6, 0, 1], [1, 1, 7, 5, 5, 0], [8, 2]]
        mancala.play(2, 3)
        assert mancala.game_log[-1] == [[6, 2, 7, 6, 0, 1], [1, 1, 0, 6, 6, 1], [8, 3]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[6, 2, 7, 6, 0, 0], [1, 1, 0, 6, 6, 1], [9, 3]]
        mancala.play(1, 6) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[6, 2, 7, 6, 0, 0], [1, 1, 0, 6, 6, 1], [9, 3]]
        mancala.play(2, 6)
        assert mancala.game_log[-1] == [[6, 2, 7, 6, 0, 0], [1, 1, 0, 6, 6, 0], [9, 4]]
        mancala.play(2, 5) # player 2 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[7, 3, 8, 7, 0, 0], [1, 1, 0, 6, 0, 1], [9, 5]]
        mancala.play(1, 3)
        assert mancala.game_log[-1] == [[7, 3, 0, 8, 1, 1], [2, 2, 1, 7, 0, 1], [10, 5]]
        mancala.play(2, 6)
        assert mancala.game_log[-1] == [[7, 3, 0, 8, 1, 1], [2, 2, 1, 7, 0, 0], [10, 6]]
        mancala.play(2, 4) # player 2 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[8, 4, 1, 9, 1, 1], [2, 2, 1, 0, 1, 1], [10, 7]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[8, 4, 1, 9, 1, 0], [2, 2, 1, 0, 1, 1], [11, 7]]
        mancala.play(1, 4) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[8, 4, 1, 0, 2, 1], [3, 3, 2, 1, 2, 2], [12, 7]]
        mancala.play(2, 5)
        assert mancala.game_log[-1] == [[8, 4, 1, 0, 2, 1], [3, 3, 2, 1, 0, 3], [12, 8]]
        mancala.play(2, 6) # player 2 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[9, 5, 1, 0, 2, 1], [3, 3, 2, 1, 0, 0], [12, 9]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[9, 5, 1, 0, 2, 0], [3, 3, 2, 1, 0, 0], [13, 9]]
        mancala.play(1, 5) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[9, 5, 1, 0, 0, 1], [3, 3, 2, 1, 0, 0], [14, 9]]
        mancala.play(2, 4)
        assert mancala.game_log[-1] == [[9, 0, 1, 0, 0, 1], [3, 3, 2, 0, 0, 0], [14, 15]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[9, 0, 1, 0, 0, 0], [3, 3, 2, 0, 0, 0], [15, 15]]
        mancala.play(1, 3) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[9, 0, 0, 0, 0, 0], [3, 3, 0, 0, 0, 0], [18, 15]]
        mancala.play(2, 2)
        assert mancala.game_log[-1] == [[9, 0, 0, 0, 0, 0], [3, 0, 1, 1, 0, 0], [18, 16]]
        mancala.play(1, 1)
        assert mancala.game_log[-1] == [[0, 1, 1, 1, 1, 1], [4, 1, 2, 1, 0, 0], [19, 16]]
        mancala.play(2, 4)
        assert mancala.game_log[-1] == [[0, 0, 1, 1, 1, 1], [4, 1, 2, 0, 0, 0], [19, 18]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[0, 0, 1, 1, 1, 0], [4, 1, 2, 0, 0, 0], [20, 18]]
        mancala.play(1, 5) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[0, 0, 1, 1, 0, 0], [0, 1, 2, 0, 0, 0], [25, 18]]
        mancala.play(2, 3)
        assert mancala.game_log[-1] == [[0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [25, 19]]
        mancala.play(1, 4)
        assert mancala.game_log[-1] == [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [27, 19]]
        assert mancala.game_over == False
        mancala.play(2, 4)
        assert mancala.game_log[-1] == [[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [27, 20]]
        assert mancala.game_over == True



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

