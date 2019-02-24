import unittest.mock as mock

from mancala.mancala_board import MancalaBoard
from mancala.mcts import MCTSNode, MCTS

class TestNodeHasCorrectValues:
    def test_create_node_with_default_values(self):
        mock_game = mock.Mock()
        mock_game.game_board_log = [[[2,0,3,0,0,0], [1,1,1,1,1,0], [15,15]]]
        mock_game.game_is_over = False
        expected_player = 2
        expected_move = 5

        node = MCTSNode(mock_game, expected_player, expected_move)
        assert node.game_state == mock_game
        assert node.player == expected_player
        assert node.current_board_state == mock_game.game_board_log[0]
        assert node.move == expected_move
        assert node.parent_node == None
        assert node.child_nodes == set()
        assert node.explored_child_moves == set()
        assert node.number_of_visits == 0
        assert node.total_reward == 0
        assert node.is_fully_expanded == False
        assert node.is_leaf == False

class TestNodeAddExploredChildMove:
    def test_adds_an_explored_child_move(self):
        mock_game = mock.Mock()
        mock_game.game_board_log = [[[2, 0, 3, 0, 0, 0], [1, 1, 1, 1, 1, 0], [15, 15]]]
        mock_game.game_is_over = False
        player = 1
        move = 3
        explored_child_move = 1

        node = MCTSNode(mock_game, player, move)
        node.add_explored_child_move(explored_child_move)
        assert node.explored_child_moves == { explored_child_move }

class TestNodeAddChildNode:
    def test_adds_a_child_node(self):
        mock_game = mock.Mock()
        mock_game.game_board_log = [[[2, 0, 3, 0, 0, 0], [1, 1, 1, 1, 1, 0], [15, 15]]]
        mock_game.game_is_over = False
        player = 1
        move = 3
        child_node = "child node"

        node = MCTSNode(mock_game, player, move)
        node.add_child_node(child_node)
        assert node.child_nodes == {child_node}

class TestNodeCheckChildMoves:
    def test_returns_child_moves_to_explore(self):
        mock_game = mock.Mock()
        mock_game.game_board_log = [[[2, 0, 3, 0, 0, 0], [1, 1, 1, 1, 1, 0], [15, 15]]]
        mock_game.game_is_over = False
        mock_game.get_legal_moves.return_value = [1, 3]
        player = 1
        move = 3

        node = MCTSNode(mock_game, player, move)
        assert node.check_child_moves_to_explore() == {1, 3}

    def test_returns_an_empty_set_when_there_are_no_child_moves_to_explore(self):
        mock_game = mock.Mock()
        mock_game.game_board_log = [[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [15, 15]]]
        mock_game.game_is_over = False
        mock_game.get_legal_moves.return_value = []
        player = 1
        move = 3

        node = MCTSNode(mock_game, player, move)
        assert node.check_child_moves_to_explore() == set()

