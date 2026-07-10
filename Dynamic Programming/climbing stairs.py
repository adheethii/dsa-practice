"""
Problem: Climbing Stairs
Difficulty: Easy
Category: Dynamic Programming
LeetCode: #70

Problem Statement:
You are climbing a staircase with n steps.
Each time you can climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example:
Input:  n = 2
Output: 2  (1+1, 2)

Input:  n = 3
Output: 3  (1+1+1, 1+2, 2+1)
"""

# ─────────────────────────────────────────────
# APPROACH 1: Recursion with Memoization
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def climb_stairs_memo(n, memo={}):
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]


# ─────────────────────────────────────────────
# APPROACH 2: Dynamic Programming (Bottom-up)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def climb_stairs_dp(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# ─────────────────────────────────────────────
# APPROACH 3: Fibonacci (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def climb_stairs(n):
    """
    Key insight:
    Ways to reach step n = ways to reach (n-1) + ways to reach (n-2)
    This is exactly the Fibonacci sequence!

    n=1: 1 way
    n=2: 2 ways
    n=3: dp[2] + dp[1] = 2+1 = 3
    n=4: dp[3] + dp[2] = 3+2 = 5
    n=5: dp[4] + dp[3] = 5+3 = 8
    """
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Fibonacci (Optimal):
- Time:  O(n) — single loop
- Space: O(1) — only two variables

KEY PATTERN LEARNED:
Climbing stairs = Fibonacci sequence.
This is the classic intro to Dynamic Programming.
Pattern: when current state depends on previous states → DP.
Always ask: "Can I express f(n) in terms of f(n-1) and f(n-2)?"
"""
