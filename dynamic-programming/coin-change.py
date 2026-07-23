"""
Problem: Coin Change
Difficulty: Medium
Category: Dynamic Programming
LeetCode: #322

Problem Statement:
Given coins of different denominations and a total amount,
return the FEWEST number of coins needed to make up that
amount. Return -1 if it's impossible.

Example:
Input:  coins = [1,2,5], amount = 11
Output: 3  (5 + 5 + 1 = 11, using 3 coins)
"""

# ─────────────────────────────────────────────
# APPROACH: Bottom-up DP
# Time: O(amount * len(coins)) | Space: O(amount)
# ─────────────────────────────────────────────

def coin_change(coins, amount):
    """
    Key insight:
    dp[i] = minimum coins needed to make amount i.
    For each amount, try EVERY coin — if using that coin
    leaves a smaller amount we already solved, use it.

    dp[i] = min(dp[i], dp[i - coin] + 1) for each coin

    Example walkthrough:
    coins=[1,2,5], amount=11

    dp[0] = 0 (base case: 0 coins needed for amount 0)
    dp[1] = dp[0]+1 = 1        (use coin 1)
    dp[2] = min(dp[1]+1, dp[0]+1) = 1   (use coin 2 directly)
    dp[3] = min(dp[2]+1, dp[1]+1) = 2   (2+1)
    ...
    dp[11] = min(dp[10]+1[coin1], dp[9]+1[coin2], dp[6]+1[coin5])
           = 3   (5+5+1)
    """
    # dp[i] = min coins to make amount i; start with "infinity" (impossible)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0   # 0 coins needed to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert coin_change([1,2,5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1], 1) == 1
    assert coin_change([1,3,4,5], 7) == 2   # 3+4

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Bottom-up DP:
- Time:  O(amount * len(coins)) — for each amount, try every coin
- Space: O(amount) — the dp array

KEY PATTERN LEARNED:
Classic "unbounded knapsack" pattern — build up solutions for
SMALLER amounts first, then use them to solve larger amounts.
dp[i] = min(dp[i], dp[i-coin]+1) is the recurrence to memorize.
This exact pattern extends to: Coin Change 2 (count ways, not
min coins), Perfect Squares.
"""
