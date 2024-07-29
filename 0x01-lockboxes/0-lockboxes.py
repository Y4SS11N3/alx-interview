#!/usr/bin/python3
"""Module for the canUnlockAll function."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    boxes (list of lists): A list of lists where each inner list represents
                           a box and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return True

    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if (isinstance(new_key, int) and
                0 <= new_key < n and
                new_key not in unlocked):
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
