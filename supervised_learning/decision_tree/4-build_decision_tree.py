#!/usr/bin/env python3
"""Decision Tree bounds computation module."""

import numpy as np


class Node:
    """Represents an internal node of a decision tree."""

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """Initialize a decision tree node."""
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth
        self.lower = {}
        self.upper = {}

    def max_depth_below(self):
        """Return the maximum depth below this node."""
        if self.left_child is None and self.right_child is None:
            return self.depth

        left_depth = self.depth
        right_depth = self.depth

        if self.left_child is not None:
            left_depth = self.left_child.max_depth_below()

        if self.right_child is not None:
            right_depth = self.right_child.max_depth_below()

        return max(left_depth, right_depth)

    def get_leaves_below(self):
        """Return the list of all leaves in the subtree below this node."""
        leaves = []
        if self.left_child is not None:
            leaves.extend(self.left_child.get_leaves_below())
        if self.right_child is not None:
            leaves.extend(self.right_child.get_leaves_below())
        return leaves

    def update_bounds_below(self):
        """Compute and update bounds for all nodes below this node."""
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -np.inf}

        # Update bounds for children
        for child in [self.left_child, self.right_child]:
            if child is not None:
                # Start with parent's bounds
                child.lower = self.lower.copy()
                child.upper = self.upper.copy()

        # Update bounds based on the splitting feature and threshold
        if self.left_child is not None and self.feature is not None:
            # Left child: values <= threshold
            # So update the UPPER bound for this feature
            if self.feature in self.left_child.upper:
                self.left_child.upper[self.feature] = min(
                    self.left_child.upper[self.feature], self.threshold
                )
            else:
                self.left_child.upper[self.feature] = self.threshold

        if self.right_child is not None and self.feature is not None:
            # Right child: values > threshold
            # So update the LOWER bound for this feature
            if self.feature in self.right_child.lower:
                self.right_child.lower[self.feature] = max(
                    self.right_child.lower[self.feature], self.threshold
                )
            else:
                self.right_child.lower[self.feature] = self.threshold

        # Recursively update bounds for children
        for child in [self.left_child, self.right_child]:
            if child is not None:
                child.update_bounds_below()


class Leaf(Node):
    """Represents a leaf node of a decision tree."""

    def __init__(self, value, depth=None):
        """Initialize a leaf node."""
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Return the depth of the leaf."""
        return self.depth

    def get_leaves_below(self):
        """Return the leaf itself as a list."""
        return [self]

    def update_bounds_below(self):
        """Leaf nodes don't need to update bounds further."""
        pass

    def __str__(self):
        """Return a string representation of the leaf."""
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    """Represents a decision tree."""

    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        """Initialize the decision tree."""
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Return the maximum depth of the decision tree."""
        return self.root.max_depth_below()

    def get_leaves(self):
        """Return the list of all leaves in the decision tree."""
        return self.root.get_leaves_below()

    def update_bounds(self):
        """Update bounds for all nodes in the decision tree."""
        self.root.update_bounds_below()
