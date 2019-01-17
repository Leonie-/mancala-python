import math
import numpy
import collections
import random

from mancala_board import MancalaBoard

class EmptyNode(object):
    def __init__(self):
        self.parent = None
        self.visited_states = set()

class UCTNode():
    def __init__(self, current_board, legal_moves, move=None, parent=EmptyNode()):
        self.current_board_state = current_board
        self.legal_moves = legal_moves
        self.move = move
        self.parent_node = parent
        self.child_nodes = set()
        self.explored_child_moves = set()
        self.unexplored_child_moves= set()

    def check_child_moves_to_explore(self):
        self.unexplored_child_moves = set(self.legal_moves)^set(self.explored_child_moves)
        return self.unexplored_child_moves

    def add_explored_child_move(self, move):
        self.explored_child_moves.add(move)

    def add_child_node(self, child):
        self.child_nodes.add(child)

class MCTS():
    def __init__(self, mancala, player_number):
        self.mancala = mancala
        self.player_number = player_number

    def selection(self, number_of_simulations):
        phasing_player = self.player_number
        legal_moves = self.mancala.get_legal_moves(phasing_player)
        last_move = self.mancala.game_board_log[-1]

        # Create root node (top of tree)
        root_node = UCTNode(last_move, legal_moves)

        # If there are child nodes that have't been explored yet, explore one (selection)
        if root_node.check_child_moves_to_explore():
            child_move = random.sample(root_node.unexplored_child_moves, 1) # Needs selection logic
            child_node = UCTNode(last_move, legal_moves, child_move, root_node)


        # Add a new node to the tree (expansion)
        # Run simulations of random moves from this node until a leaf is reached (simulation)
        # Update the node with relevant stats (update)

        # for simulation in range(number_of_simulations):
            # leaf = rootNode.select_leaf()






    def pick_pot(self, number_of_simulations):
        return self.selection(number_of_simulations)
