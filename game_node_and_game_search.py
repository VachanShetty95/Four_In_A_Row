"""
Definitions for GameNode, GameSearch and MCTS
"""
from time import process_time
import random
import math


class GameNode:
    """
    This class defines game nodes in game search trees. It keep track of: 
    state
    """

    def __init__(self, state, node=None):
        self.state = state


class GameSearch:
    """
    Class containing different game search algorithms, call it with a defined game/node
    """

    def __init__(self, game, depth=3):
        self.state = game
        self.depth = depth

    def mcts(self):
        start_time = process_time()
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()
        elapsed_time = 0
        while elapsed_time < self.time:
            leaf = self.select(tree)
            child = self.expand(leaf)
            result = self.simulate(child)
            self.back_propagate(result, child)
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move

    def minimax_search(self):
        start_time = process_time()
        _, move = self.max_value(self.state, self.depth)
        return move

    def max_value(self, state, depth):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None
        v = -100000
        actions = state.actions()
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1)

            if v2 > v:
                v = v2
                move = action
        return v, move

    def min_value(self, state, depth):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None
        v = 100000
        actions = state.actions()
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1)
            if v2 < v:
                v = v2
                move = action
        return v, move

    # === MinMax with Alpha-Beta pruning ===#
    def min_max_with_alpha_beta(self, alpha, beta):
        state = self.state
        start_time = process_time()
        _, move = self.max_ab(state, alpha, beta, 0)
        assert (
            move is not None
        ), "min_max_with_alpha_bet returns none, which is not expected"
        return move

    def max_ab(self, state, alpha, beta, depth):
        move = None
        a = alpha
        terminal, value = state.is_terminal()
        if terminal or depth >= self.depth:
            return value, None
        v = -100000
        actions = state.actions()
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.min_ab(new_state, alpha, beta, depth + 1)
            if v2 > v:
                v = v2
                move = action
            if v >= a:
                return v, move
            a = max(a, v)
        return v, move

    def min_ab(self, state, alpha, beta, depth):
        move = None
        b = beta
        terminal, value = state.is_terminal()
        if terminal or depth >= self.depth:
            return value, None
        v = 100000
        actions = state.actions()
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.max_ab(new_state, alpha, beta, depth + 1)
            if v2 < v:
                v = v2
                move = action
            if v <= b:
                return v, move
            b = min(b, v)
        return v, move
