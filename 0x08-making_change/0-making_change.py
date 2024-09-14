#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list of int): List of coin denominations
    total (int): Target amount

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count

    return -1
