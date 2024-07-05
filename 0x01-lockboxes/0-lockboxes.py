#!/usr/bin/python3
"""
This module provides a function to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from the first box (box 0).

    Args:
        boxes (list of list of int): A list where each element is a list of keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
