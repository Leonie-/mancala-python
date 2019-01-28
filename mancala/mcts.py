import math
import random
import time

from mancala_board import MancalaBoard
import player
from game import Game

class Node():
    def __init__(self, game_state, move=None, parent=None, gets_another_turn=False):
        self.player_number = game_state.current_player + 1
        self.gets_another_turn = gets_another_turn
        self.current_board_state = game_state.game_board_log[-1]
        self.legal_moves = game_state.get_legal_moves(self.player_number)
        self.move = move
        self.parent_node = parent
        self.child_nodes = set()
        self.explored_child_moves = set()
        self.number_of_visits = 0
        self.total_reward = 0
        self.is_fully_expanded = False
        self.is_leaf = game_state.check_for_game_over(self.current_board_state)

    def check_child_moves_to_explore(self):
        return set(self.legal_moves)^set(self.explored_child_moves)

    def add_explored_child_move(self, move):
        self.explored_child_moves.add(move)

    def add_child_node(self, child):
        self.child_nodes.add(child)

class MCTS():
    def __init__(self, mancala, time_limit_seconds, number_of_simulations=5, exploration_constant=1):
        self.mancala = mancala
        self.time_limit = time_limit_seconds
        self.number_of_simulations = number_of_simulations
        self.exploration_constant = exploration_constant

    def pick_pot(self, player_number):
        # Create root node (top of tree)
        root_node = Node(self.mancala)
        time_limit = time.time() + self.time_limit / 1000
        while time.time() < time_limit:
            self.selection(root_node)

        promising_child = self.get_most_promising_child_with_uct(root_node, self.exploration_constant)
        return promising_child.move


    def selection(self, node):
        if not node.is_leaf:
            if node.is_fully_expanded:
                # Drill down into the tree using UCT to select the most promising child node
                promising_child = self.get_most_promising_child_with_uct(node, self.exploration_constant)
                return self.selection(promising_child)
            else:
                # Expand, simulate and backpropagate
                node = self.expand_tree(node)
                return self.selection(node)
        return

    def expand_tree(self, parent_node):
        # If there are child nodes that have't been explored yet, explore them (selection)
        moves_to_explore = parent_node.check_child_moves_to_explore()
        for child_move in moves_to_explore:
            # Add a new node to the tree (expansion)
            node = self.play_move_and_add_node(parent_node, child_move)
            # Run simulations of random moves from this node until a leaf is reached (simulation)
            for index in range(self.number_of_simulations):
                reward = self.run_simulation(node.current_board_state, node.player_number)
                # Backpropagate and update the nodes with relevant stats (update)
                self.backpropogate(node, reward)

        parent_node.is_fully_expanded = True
        return parent_node

    def play_move_and_add_node(self, parent_node, move):
        player = self.get_opposite_player(parent_node)
        mancala_board = MancalaBoard(6, 6, parent_node.current_board_state)
        gets_another_turn = mancala_board.play(player, move)
        node = Node(mancala_board, move, parent_node, gets_another_turn)
        # Add new node to the tree
        parent_node.add_child_node(node)
        return node

    def get_opposite_player(self, parent_node):
        if parent_node.gets_another_turn is True:
            return parent_node.player_number
        return 1 if parent_node.player_number is 2 else 2

    def run_simulation(self, board_state, player_number, max_depth=5):
        mancala_board = MancalaBoard(6, 6, board_state)
        simulated_game = Game(
            mancala_board,
            player.Player(1, "random", mancala_board, max_depth),
            player.Player(2, "random", mancala_board, max_depth)
        )
        # Run simulation and determine winner
        game_logs = simulated_game.play(player_number)
        # print(f"{game_logs}")
        winner = game_logs[-1][-1]['current_winning_player']
        # Return reward
        reward = 0
        if winner is player_number:
            reward = 1
        if winner is "draw":
            reward = 0.5

        return reward

    def backpropogate(self, node, reward):
        while node is not None:
            node.number_of_visits += 1
            node.total_reward += reward
            node = node.parent_node

    def get_most_promising_child_with_uct(self, node, exploration_value):
        best_value =  float("-inf")
        best_nodes = []
        for child_node in node.child_nodes:
            # Upper confidence bounds for trees algorithm (UCT)
            value = child_node.total_reward / child_node.number_of_visits + \
                    exploration_value * math.sqrt(2 * math.log(node.number_of_visits) / child_node.number_of_visits)
            if value >= best_value:
                best_value = value
                best_nodes.append(child_node)
        return random.choice(best_nodes)
















