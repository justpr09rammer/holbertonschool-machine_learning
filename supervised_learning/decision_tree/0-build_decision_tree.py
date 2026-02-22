        self.depth = depth

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
                                                                                                                                                                                    137,42        Bot
