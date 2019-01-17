import unittest.mock as mock

from mancala.mcts import UCTNode, EmptyNode, MCTS

class TestEmptyNode:
    def test_adds_an_empty_node(self):
        empty_node = EmptyNode()
        assert empty_node.parent == None
        assert empty_node.visited_states == set()

class TestUCTNodeAddExploredChildMove:
    def test_adds_an_explored_child_move(self):
        current_board_state = []
        legal_moves = [2, 3, 6]
        test_child_move = 3

        uct_node = UCTNode(current_board_state, legal_moves)
        uct_node.add_explored_child_move(test_child_move)
        assert uct_node.explored_child_moves == { 3 }

class TestUCTNodeAddChildNode:
    def test_adds_an_explored_child_move(self):
        current_board_state = []
        legal_moves = [2, 3, 6]
        test_child_node = "child node object"

        uct_node = UCTNode(current_board_state, legal_moves)
        uct_node.add_child_node(test_child_node)
        assert uct_node.child_nodes == { test_child_node }

class TestUCTNodeCheckChildMoves:
    def test_returns_child_moves_to_explore(self):
        current_board_state = []
        legal_moves = [2, 3, 6]

        uct_node = UCTNode(current_board_state, legal_moves)
        assert uct_node.check_child_moves_to_explore() == {2, 3, 6}
        assert uct_node.unexplored_child_moves == {2, 3, 6}

    def test_returns_an_empty_set_when_there_are_no_child_moves_to_explore(self):
        current_board_state = []
        legal_moves = [2]

        uct_node = UCTNode(current_board_state, legal_moves)
        uct_node.add_explored_child_move(2)
        assert uct_node.check_child_moves_to_explore() == set()
        assert uct_node.unexplored_child_moves == set()

# class TestMCTS:
#     def test_selects_a_pot(self):
#         mancala_mock = mock.Mock()
#         mancala_mock.game_board_log = [[[4, 5, 4, 3, 2, 1], [4, 0, 3, 0, 16, 0], [3, 16]]]
#         mancala_mock.get_legal_moves.return_value = [1, 2, 3, 4, 5, 6]
#         player_number = 1
#
#         mcts = MCTS(mancala_mock, player_number)
#         assert mcts.selection(10) == 1