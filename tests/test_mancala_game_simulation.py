from mancala.mancala import Mancala
import pytest

class TestGamePlaySimulation:

    @pytest.fixture(scope='function')
    def mancala(self):
        return Mancala(6, 4)

    def test_game_simulation(self, mancala):
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
        mancala.play(1, 1) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[0, 3, 8, 7, 1, 1], [1, 1, 0, 6, 6, 1], [10, 3]]
        mancala.play(2, 6)
        assert mancala.game_log[-1] == [[0, 3, 8, 7, 1, 1], [1, 1, 0, 6, 6, 0], [10, 4]]
        mancala.play(2, 2) # player 2 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[0, 3, 8, 0, 1, 1], [1, 0, 0, 6, 6, 0], [10, 12]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[0, 3, 8, 0, 1, 0], [1, 0, 0, 6, 6, 0], [11, 12]]
        mancala.play(1, 5) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[0, 3, 8, 0, 0, 0], [0, 0, 0, 6, 6, 0], [13, 12]]
        mancala.play(2, 5)
        assert mancala.game_log[-1] == [[1, 4, 9, 1, 0, 0], [0, 0, 0, 6, 0, 1], [13, 13]]
        mancala.play(1, 4)
        assert mancala.game_log[-1] == [[1, 4, 9, 0, 0, 0], [0, 0, 0, 6, 0, 1], [14, 13]]
        mancala.play(2, 6)
        assert mancala.game_log[-1] == [[1, 4, 9, 0, 0, 0], [0, 0, 0, 6, 0, 0], [14, 14]]
        mancala.play(2, 4) # player 2 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[2, 5, 10, 0, 0, 0], [0, 0, 0, 0, 1, 1], [14, 15]]
        mancala.play(1, 3)
        assert mancala.game_log[-1] == [[2, 5, 0, 1, 1, 1], [1, 1, 1, 1, 2, 2], [15, 15]]
        mancala.play(2, 5)
        assert mancala.game_log[-1] == [[2, 5, 0, 1, 1, 1], [1, 1, 1, 1, 0, 3], [15, 16]]
        mancala.play(1, 6)
        assert mancala.game_log[-1] == [[2, 5, 0, 1, 1, 0], [1, 1, 1, 1, 0, 3], [16, 16]]
        mancala.play(1, 5) # player 1 extra move for ending last turn in the store
        assert mancala.game_log[-1] == [[2, 5, 0, 1, 0, 0], [0, 1, 1, 1, 0, 3], [18, 16]]
        mancala.play(2, 6)
        assert mancala.game_log[-1] == [[3, 6, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0], [18, 17]]
        mancala.play(1, 4)
        assert mancala.game_log[-1] == [[3, 6, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [20, 17]]
        mancala.play(2, 4)
        assert mancala.game_log[-1] == [[3, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [20, 24]]
        mancala.play(1, 1)
        assert mancala.game_log[-1] == [[0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [22, 24]]
        assert mancala.game_over == True
        assert mancala.winning_player == 2