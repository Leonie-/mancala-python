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
        assert mancala.winning_player == 1
