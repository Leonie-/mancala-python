import unittest.mock as mock

from mancala.player import Player

def test_creates_a_new_player():
    player = Player(1, "random", mock.Mock())
    assert player.player_number == 1
    assert player.player_type == "random"
    assert player.opposite_player_number == 2
    assert player.maximum_depth == float("inf")

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

class TestRightPotPlayer:

    def test_picks_the_rightmost_pot_from_legal_moves_available(self):
        mancala_mock = mock.Mock()
        mancala_mock.get_legal_moves.return_value = [1, 4, 6]
        player = Player(1, "rightpot", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 6)

class TestPotWithLeastStonesPlayer:

    def test_picks_the_first_pot_with_least_stones_from_legal_moves_available(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0, 13, 21, 0, 5, 5], [0, 0, 0, 0, 0, 0], [14, 6]]]
        mancala_mock.get_legal_moves.return_value = [2, 3, 5, 6]
        player = Player(1, "potwithleast", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 5)

    def test_picks_the_first_pot_with_least_stones_from_legal_moves_available_when_game_has_not_ended(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log =[[[5, 4, 4, 0, 5, 5], [5, 4, 4, 0, 5, 5], [1, 1]]]
        mancala_mock.get_legal_moves.return_value = [1, 2, 3, 5, 6]
        player = Player(1, "potwithleast", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 2)

class TestPotWithMostStonesPlayer:

    def test_picks_the_first_pot_with_most_stones_from_legal_moves_available(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0, 13, 21, 0, 5, 5], [0, 0, 0, 0, 0, 0], [14, 6]]]
        mancala_mock.get_legal_moves.return_value = [2, 3, 5, 6]
        player = Player(1, "potwithmost", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 3)

    def test_picks_the_first_pot_with_most_stones_from_legal_moves_available_when_game_has_not_ended(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log =[[[5, 4, 4, 0, 5, 5], [5, 4, 4, 0, 5, 5], [1, 1]]]
        mancala_mock.get_legal_moves.return_value = [1, 2, 3, 5, 6]
        player = Player(1, "potwithmost", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 1)

class TestTakeAnotherTurnPlayer:

    def test_picks_the_pot_which_gives_an_extra_turn_from_legal_moves_available(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0, 4, 19, 3, 16, 5], [0, 0, 3, 5, 1, 0], [3, 16]]]
        mancala_mock.get_legal_moves.return_value = [2, 3, 4, 5, 6]
        player = Player(1, "takeanotherturn", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 4)

    @mock.patch('random.choice', return_value=6)
    def test_picks_random_pot_if_no_legal_moves_give_extra_turn_(self, choice_mock):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0, 4, 19, 0, 1, 5], [4, 0, 3, 0, 16, 0], [3, 16]]]
        mancala_mock.get_legal_moves.return_value = [2, 3, 5, 6]
        player = Player(1, "takeanotherturn", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 6)

class TestAvoidAnotherTurnPlayer:

    def test_picks_the_pot_which_does_not_give_an_extra_turn_from_legal_moves_available(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0, 5, 19, 3, 2, 1], [0, 0, 3, 5, 1, 0], [3, 16]]]
        mancala_mock.get_legal_moves.return_value = [2, 3, 4, 5, 6]
        player = Player(1, "avoidanotherturn", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 3)

    @mock.patch('random.choice', return_value=1)
    def test_picks_random_pot_if_all_legal_moves_give_extra_turn_(self, choice_mock):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0, 5, 4, 3, 2, 1], [4, 0, 3, 0, 16, 0], [3, 16]]]
        mancala_mock.get_legal_moves.return_value = [2, 3, 5, 6]
        player = Player(1, "avoidanotherturn", mancala_mock)
        player.play()
        mancala_mock.play.assert_called_with(1, 1)

class TestMiniMaxScoreAtLeaf:

    def test_minimax_scoring_when_leaf_is_reached_and_current_player_wins(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,0,0,0,0], [0,0,0,0,0,0], [14,6]]]
        mancala_mock.winning_player = 1
        game_over = True

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, 0, game_over) == 100

    def test_minimax_scoring_with_depth_when_leaf_is_reached_and_current_player_wins(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,0,0,0,0], [0,0,0,0,0,0], [14,6]]]
        mancala_mock.winning_player = 1
        depth = 8
        game_over = True

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, depth, game_over) == 100 - depth

    def test_minimax_scoring_when_leaf_is_reached_and_opposite_player_wins(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,0,0,0,0], [0,0,0,0,0,0], [14,6]]]
        mancala_mock.winning_player = 2
        game_over = True

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, 0, game_over) == 0

    def test_minimax_scoring_with_depth_when_leaf_is_reached_and_opposite_player_wins(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,0,0,0,0], [0,0,0,0,0,0], [14,6]]]
        mancala_mock.winning_player = 2
        depth = 6
        game_over = True

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, depth, game_over) == 0 - depth

    def test_minimax_scoring_when_leaf_is_reached_and_game_is_a_draw(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,0,0,0,0], [0,0,0,0,0,0], [28,28]]]
        mancala_mock.winning_player = 0
        game_over = True

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, 0, game_over) == 50

class TestMiniMaxScoreMidGame:

    def test_minimax_scoring_when_leaf_is_not_reached_but_current_player_is_winning(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,4,5,0,8,0], [0,0,3,0,0,0], [12,23]]]
        game_over = False

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, 0, game_over) == 100

    def test_minimax_scoring_with_depth_when_leaf_is_not_reached_but_current_player_is_winning(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,4,5,0,8,0], [0,0,3,0,0,0], [12,23]]]
        depth = 3
        game_over = False

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, depth, game_over) == 100 - depth

    def test_minimax_scoring_when_leaf_is_not_reached_but_opposite_player_is_winning(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,3,0,0,0], [0,4,5,0,8,0], [23,12]]]
        game_over = False

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, 0, game_over) == 0

    def test_minimax_scoring_with_depth_when_leaf_is_not_reached_but_opposite_player_is_winning(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[0,0,3,0,0,0], [0,4,5,0,8,0], [23,12]]]
        depth = 3
        game_over = False

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, depth, game_over) == 0 - depth


    def test_minimax_scoring_when_leaf_is_not_reached_but_game_is_a_draw(self):
        mancala_mock = mock.Mock()
        mancala_mock.game_board_log = [[[2,0,3,0,0,0], [1,1,1,1,1,0], [15,15]]]
        game_over = False

        player = Player(1, "minimax", mancala_mock)
        assert player.minimaxScore(mancala_mock, 0, game_over) == 50