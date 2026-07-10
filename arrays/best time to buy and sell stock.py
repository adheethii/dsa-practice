"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Category: Arrays
LeetCode: #121

Problem Statement:
Given an array prices where prices[i] is the price on day i,
return the maximum profit from ONE buy and ONE sell.
You must buy before you sell. Return 0 if no profit possible.

Example:
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5  (buy at 1, sell at 6)

Input:  prices = [7, 6, 4, 3, 1]
Output: 0  (prices always decrease)
"""

# ─────────────────────────────────────────────
# APPROACH: One Pass (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def max_profit(prices):
    """
    Key insight:
    Track the minimum price seen so far (best buy day).
    At each price, calculate profit if we sell today.
    Update max profit if current profit is better.

    Example walkthrough:
    prices = [7, 1, 5, 3, 6, 4]

    day 0: price=7, min_price=7, profit=0,  max_profit=0
    day 1: price=1, min_price=1, profit=0,  max_profit=0
    day 2: price=5, min_price=1, profit=4,  max_profit=4
    day 3: price=3, min_price=1, profit=2,  max_profit=4
    day 4: price=6, min_price=1, profit=5,  max_profit=5 ✅
    day 5: price=4, min_price=1, profit=3,  max_profit=5
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([1]) == 0

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
One Pass:
- Time:  O(n) — single pass through prices
- Space: O(1) — only two variables

KEY PATTERN LEARNED:
Track running minimum while scanning array.
At each step: profit = current_price - min_price_so_far
This pattern appears in many "maximum difference" problems.
Key: we want to buy LOW and sell HIGH — so track the lowest
buy price seen so far, calculate sell profit at each point.
"""
