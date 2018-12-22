import unittest.mock as mock

import game_state

class TestGameState:

    def test_game_state_returns_current_player(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]],
                     [[4, 4, 0, 0, 6, 6], [5, 5, 4, 4, 4, 4], [2, 0]]]
        gets_extra_turn = False
        is_game_over = False

        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["current_player"] == 1

    def test_game_state_returns_pot_played(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]],
                     [[4, 4, 0, 0, 6, 6], [5, 5, 4, 4, 4, 4], [2, 0]]]

        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["pot_played"] == 4

    def test_game_state_returns_turn_number(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]],
                     [[4, 4, 0, 0, 6, 6], [5, 5, 4, 4, 4, 4], [2, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["turn_number"] == 2

    def test_game_state_returns_stones_captured_for_player_one(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]],
                     [[4, 4, 0, 0, 6, 6], [5, 5, 4, 4, 4, 4], [2, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_captured"] == 1

    def test_game_state_returns_stones_captured_for_player_two(self):
        player_number = 2
        pot_number = 1
        board_log = [[[2, 7, 3, 7, 8, 1], [13, 0, 3, 2, 1, 0], [14, 21]],
                     [[3, 8, 4, 8, 9, 0], [0, 1, 4, 3, 2, 1], [14, 24]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_captured"] == 3

    def test_game_state_returns_extra_turn(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]]]
        gets_extra_turn = True
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["get_extra_turn"] == True

    def test_game_state_returns_if_final_turn(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], [1, 0]]]
        gets_extra_turn = True
        is_game_over = True
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["is_final_turn"] == True

    def test_game_state_returns_empty_pots_on_own_side(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 0, 0, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 0, 0, 0, 1, 5], [1, 4, 4, 0, 4, 0], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["empty_pots_on_own_side_start"] == [2, 3, 5]
        assert result["empty_pots_on_own_side_end"] == [2, 3, 4]

    def test_game_state_returns_empty_pots_on_opponents_side(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 0, 0, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 0, 0, 0, 1, 5], [1, 4, 4, 0, 4, 0], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["empty_pots_on_opponents_side_start"] == [1, 4, 6]
        assert result["empty_pots_on_opponents_side_end"] == [4, 6]

    def test_game_state_returns_number_of_moves_available_on_own_side_at_start(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 0, 0, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 0, 0, 0, 1, 5], [1, 4, 4, 0, 4, 0], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["moves_available_on_own_side_at_start"] == [1, 4, 6]
        assert result["moves_available_on_own_side_at_end"] == [1, 5, 6]

    def test_game_state_returns_number_of_moves_available_on_opponents_side_at_start(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 0, 0, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 0, 0, 0, 1, 5], [1, 4, 4, 0, 4, 0], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["moves_available_on_opponents_side_at_start"] == [2, 3, 5]
        assert result["moves_available_on_opponents_side_at_end"] == [1, 2, 3, 5]

    def test_game_state_returns_stones_sown_on_own_side(self):
        player_number = 1
        pot_number = 4
        board_log = [[[4, 0, 0, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 0, 0, 0, 1, 5], [1, 4, 4, 0, 4, 0], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_sown_on_own_side"] == 2

    def test_game_state_returns_stones_sown_on_own_side_when_there_are_fewer_stones_sown_than_pots(self):
        player_number = 1
        pot_number = 2
        board_log = [[[4, 1, 1, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 0, 2, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_sown_on_own_side"] == 1

    def test_game_state_returns_stones_sown_on_own_side_when_a_turn_loops_around(self):
        player_number = 1
        pot_number = 3
        board_log = [[[4, 4, 16, 4, 4, 4], [4, 4, 4, 4, 4, 4], [0, 0]],
                     [[5, 5, 1, 6, 6, 6], [5, 5, 5, 5, 5, 5], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_sown_on_own_side"] == 9

    def test_game_state_returns_stones_sown_on_opponents_side(self):
        player_number = 2
        pot_number = 4
        board_log = [[[25, 15, 0, 3, 16, 9], [13, 27, 8, 23, 16, 0], [0, 0]],
                     [[27, 17, 2, 5, 18, 11], [15, 2, 11, 25, 18, 2], [0, 2]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_sown_on_opponents_side"] == 12

    def test_game_state_returns_stones_sown_on_opponents_side_when_there_are_fewer_stones(self):
        player_number = 1
        pot_number = 6
        board_log = [[[4, 1, 1, 4, 0, 4], [0, 4, 4, 0, 4, 0], [0, 0]],
                     [[4, 1, 1, 4, 0, 0], [1, 5, 5, 0, 4, 0], [1, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["stones_sown_on_opponents_side"] == 3

    def test_game_state_returns_current_score(self):
        player_number = 1
        pot_number = 6
        board_log = [[[4, 1, 1, 4, 0, 4], [0, 4, 4, 0, 4, 0], [23, 14]],
                     [[4, 1, 1, 4, 0, 0], [1, 5, 5, 0, 4, 0], [24, 14]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["current_score"] == [24, 14]

    def test_game_state_returns_player_score(self):
        player_number = 1
        pot_number = 6
        board_log = [[[4, 1, 1, 4, 0, 4], [0, 4, 4, 0, 4, 0], [23, 14]],
                     [[4, 1, 1, 4, 0, 0], [1, 5, 5, 0, 4, 0], [24, 14]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["player_score"] == 24

    def test_game_state_returns_opponent_score(self):
        player_number = 1
        pot_number = 6
        board_log = [[[4, 1, 1, 4, 0, 4], [0, 4, 4, 0, 4, 0], [23, 14]],
                     [[4, 1, 1, 4, 0, 0], [1, 5, 5, 0, 4, 0], [24, 14]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["opponent_score"] == 14

    def test_game_state_returns_score_difference(self):
        player_number = 1
        pot_number = 6
        board_log = [[[4, 1, 1, 4, 0, 4], [0, 4, 4, 0, 4, 0], [23, 14]],
                     [[4, 1, 1, 4, 0, 0], [1, 5, 5, 0, 4, 0], [24, 14]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["score_difference"] == 10

    def test_game_state_returns_kroos_on_own_side_start(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_own_side_start"] == [25, 15, 13, 16]

    def test_game_state_returns_kroos_on_own_side_end(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_own_side_end"] == [26, 16, 17]

    def test_game_state_returns_kroos_on_own_side_index_start(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_own_side_index_start"] == [1, 2, 3, 5]

    def test_game_state_returns_kroos_on_own_side_index_end(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_own_side_index_end"] == [1, 2, 5]

    def test_game_state_returns_kroos_on_opponents_side_start(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_opponents_side_start"] == [27, 23, 16]

    def test_game_state_returns_kroos_on_opponents_side_end(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_opponents_side_end"] == [13, 28, 17]

    def test_game_state_returns_kroos_on_opponents_side_index_start(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_opponents_side_index_start"] == [2, 4, 5]

    def test_game_state_returns_kroos_on_opponents_side_index_end(self):
        player_number = 1
        pot_number = 3
        board_log = [[[25, 15, 13, 3, 16, 9], [12, 27, 8, 23, 16, 0], [0, 0]],
                     [[26, 16, 0, 4, 17, 10], [13, 28, 9, 0, 17, 1], [26, 0]]]
        gets_extra_turn = False
        is_game_over = False
        result = game_state.get_game_state(player_number, pot_number, board_log, gets_extra_turn, is_game_over)
        assert result["kroos_on_opponents_side_index_end"] == [1, 2, 5]