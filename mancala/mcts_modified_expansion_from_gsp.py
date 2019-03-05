import math
import random
import time

from mancala_board import MancalaBoard
import player
from game import Game

class MCTSModifiedFromGspNode():
    def __init__(self, game_state, player=None, move=None, parent=None, extra_turn=False):
        self.game_state = game_state
        self.player = player
        self.current_board_state = game_state.game_board_log[-1]
        self.move = move
        self.parent_node = parent
        self.get_legal_moves = game_state.get_legal_moves
        self.child_nodes = set()
        self.explored_child_moves = set()
        self.number_of_visits = 0
        self.total_reward = 0
        self.is_fully_expanded = False
        self.is_leaf = game_state.game_is_over
        self.extra_turn = extra_turn

    def check_child_moves_to_explore(self):
        legal_moves = self.get_legal_moves(self.player)
        return set(legal_moves)^set(self.explored_child_moves)

    def add_explored_child_move(self, move):
        self.explored_child_moves.add(move)

    def add_child_node(self, child):
        self.child_nodes.add(child)

class MCTSModifiedFromGsp():
    def __init__(self, mancala, player_number, time_limit_seconds, number_of_simulations=5, exploration_constant=1):
        self.mancala = mancala
        self.time_limit = time_limit_seconds
        self.number_of_simulations = number_of_simulations
        self.exploration_constant = exploration_constant
        self.player = player_number

    def pick_pot(self):
        # Create root node (top of tree) with correct starting player set
        root_node = MCTSModifiedFromGspNode(self.mancala, self.player)

        # Set a time limit
        time_limit = time.time() + self.time_limit / 1000
        while time.time() < time_limit:
            self.selection(root_node)

        promising_child = self.get_most_promising_child_with_uct(root_node)
        return promising_child.move

    def selection(self, node):
        # Recursive function to expand tree down to leaf node
        if not node.is_leaf:
            if node.is_fully_expanded:
                # Drill down into the tree using UCT to select the most promising child node
                promising_child = self.get_most_promising_child_with_uct(node)
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
            node = self.play_move_and_create_node(parent_node, child_move)
            parent_node.add_child_node(node)
            parent_node.add_explored_child_move(child_move)

            if node.is_leaf:
                reward = self.get_reward(node.game_state.winning_player)
                # Backpropagate and update the nodes with relevant stats (update)
                self.backpropogate(node, reward)
            else:
                # Run simulations of random moves from this node until a leaf is reached (simulation)
                for index in range(self.number_of_simulations):
                    reward = self.run_simulation(node.current_board_state, node.player)
                    # Backpropagate and update the nodes with relevant stats for each simulation (update)
                    self.backpropogate(node, reward)

        parent_node.is_fully_expanded = True
        return parent_node

    def play_move_and_create_node(self, parent_node, move):
        mancala_board = MancalaBoard(6, 6, parent_node.current_board_state)
        extra_turn = mancala_board.play(parent_node.player, move)
        # Switch players
        next_player = self.get_next_player(parent_node.player, extra_turn)
        # Add new node to the tree
        return MCTSModifiedFromGspNode(mancala_board, next_player, move, parent_node, extra_turn)

    def get_next_player(self, current_player, extra_turn):
        if extra_turn is True:
            return current_player
        return 1 if current_player is 2 else 2

    def run_simulation(self, board_state, player_number, max_depth=5):
        mancala_board = MancalaBoard(6, 6, board_state)
        simulated_game = Game(
            mancala_board,
            player.Player(1, "random", mancala_board, max_depth),
            player.Player(2, "random", mancala_board, max_depth)
        )
        # Run simulation and determine winner
        game_logs = simulated_game.play(player_number)
        winner = game_logs[-1][-1]['current_winning_player']
        # Return reward
        return self.get_reward(winner)

    def get_reward(self, winner):
        if winner is self.player:
            return 1
        if winner is "draw":
            return 0.5
        else:
            return 0

    def backpropogate(self, node, reward):
        while node is not None:
            node.number_of_visits += 1
            node.total_reward += reward
            node = node.parent_node

    # EXPANSION MODIFICATION ---------------------------------------
    def get_exploration_value(self, node):
        exploration_value = self.exploration_constant
        if node.parent_node:
            if node.parent_node.move is 1 and node.move is 1:
                exploration_value += 0.5
            if node.parent_node.move is 5 and node.move is 6:
                exploration_value += 0.5
            if node.parent_node.move is 6 and node.move is 6:
                exploration_value += 0.5
        return exploration_value

    def get_most_promising_child_with_uct(self, node):
        best_value =  float("-inf")
        best_nodes = []
        for child_node in node.child_nodes:
            exploration_value = self.get_exploration_value(child_node)
            # Modified upper confidence bounds for trees algorithm (UCT)
            value = child_node.total_reward / child_node.number_of_visits + \
                    exploration_value * math.sqrt(math.log(node.number_of_visits) / child_node.number_of_visits)

            if value >= best_value:
                best_value = value
                best_nodes.append(child_node)
        return random.choice(best_nodes)
