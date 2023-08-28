#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make
    change for a given total amountself.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target total amount to make change forself.

    Returns:
        int: The minimum number of coins needed to achieve the target total.
        Returns -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize a dynamic programming table with inf values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update the dp table for amounts from coin to total
        for amount in range(coin, total + 1):
            # Calculate the minimum coins needed for the current amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

            # Return the result, considering if change is possible
    return dp[total] if dp[total] != float('inf') else -1
