#!/usr/bin/env python3
import numpy as np

def left_child_add_prefix(text):
    """Add prefix for left child in tree visualization"""
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "    |  " + x + "\n"
    return new_text

def right_child_add_prefix(text):
    """Add prefix for right child in tree visualization"""
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "       " + x + "\n"
    return new_text


class Node:
    """Node class for decision tree"""
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def __str__(self):
        """String representation of the node"""
        if self.is_root:
            node_str = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            node_str = f"    [feature={self.feature}, threshold={self.threshold}]\n"
        
        if self.left_child:
            left_str = self.left_child.__str__()
            node_str += left_child_add_prefix(left_str)
        
        if self.right_child:
            right_str = self.right_child.__str__()
            node_str += right_child_add_prefix(right_str)
        
        return node_str


class Leaf:
    """Leaf class for decision tree"""
    def __init__(self, value, depth=None):
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def __str__(self):
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    """Decision tree class"""
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.root.__str__()
