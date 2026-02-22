#!/usr/bin/env python3
import numpy as np

def left_child_add_prefix(text):
    """Add prefix for left child in tree visualization"""
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:-1]:  # Exclude last line to avoid extra newline
        new_text += "    |  " + x + "\n"
    if len(lines) > 1:
        new_text += "    |  " + lines[-1]
    return new_text

def right_child_add_prefix(text):
    """Add prefix for right child in tree visualization"""
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:-1]:  # Exclude last line to avoid extra newline
        new_text += "       " + x + "\n"
    if len(lines) > 1:
        new_text += "       " + lines[-1]
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
            result = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            result = f"node [feature={self.feature}, threshold={self.threshold}]\n"
        
        if self.left_child:
            left_str = self.left_child.__str__()
            # Add the left child with proper prefix
            left_lines = left_str.rstrip('\n').split('\n')
            for i, line in enumerate(left_lines):
                if i == 0:
                    result += "    +---> " + line + "\n"
                else:
                    result += "    |     " + line + "\n"
        
        if self.right_child:
            right_str = self.right_child.__str__()
            # Add the right child with proper prefix
            right_lines = right_str.rstrip('\n').split('\n')
            for i, line in enumerate(right_lines):
                if i == 0:
                    result += "    +---> " + line + "\n"
                else:
                    result += "          " + line + "\n"
        
        return result.rstrip('\n') + '\n' if result else ''


class Leaf:
    """Leaf class for decision tree"""
    def __init__(self, value, depth=None):
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def __str__(self):
        return f"leaf [value={self.value}]"


class Decision_Tree:
    """Decision tree class"""
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.root.__str__()
