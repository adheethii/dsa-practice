"""
Problem: House Robber
Difficulty: Medium
Category: Dynamic Programming
LeetCode: #198

Problem Statement:
Given an array representing money in each house along a street,
determine the maximum money you can rob without robbing two
ADJACENT houses (triggers alarm).

Example:
Input:  nums = [2,7,9,3,1]
Output: 12  (rob house 0 (2) + house 2 (9) + house 4 (1) = 12)
"""

# ─────────────────────────────────────────────
# APPROACH: DP with Two Running Variables (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def rob(nums):
    """
    Key insight:
    At each house, we have exactly two choices:
    1. SKIP this house → best total is whatever we had at the
       previous house (rob_prev)
    2. ROB this house → best total is this house's money PLUS
       whatever we had two houses ago (rob_prev_prev), since we
       can't touch the immediately previous house

    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    Example walkthrough:
    nums = [2,7,9,3,1]

    prev_prev=0, prev=0
    house 0 (2): current = max(0, 0+2) = 2 → prev_prev=0, prev=2
    house 1 (7): current = max(2, 0+7) = 7 → prev_prev=2, prev=7
    house 2 (9): current = max(7, 2+9) = 11 → prev_prev=7, prev=11
    house 3 (3): current = max(11, 7+3) = 11 → prev_prev=11, prev=11
    house 4 (1): current = max(11, 11+1) = 12 → prev_prev=11, prev=12

    Final answer: 12 ✅
    """
    prev_prev, prev = 0, 0

    for money in nums:
        current = max(prev, prev_prev + money)
        prev_prev = prev
        prev = current

    return prev


# ─────────────────────────────────────────────
# APPROACH 2: Full DP array (clearer to read, more space)
# ─────────────────────────────────────────────

def rob_dp_array(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert rob([2,7,9,3,1]) == 12
    assert rob([1,2,3,1]) == 4
    assert rob([2,1,1,2]) == 4
    assert rob([5]) == 5
    assert rob([]) == 0
    assert rob_dp_array([2,7,9,3,1]) == 12

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Two-variable DP:
- Time:  O(n) — single pass
- Space: O(1) — only two running totals, no array needed

KEY PATTERN LEARNED:
"Non-adjacent selection to maximize sum" is a foundational DP
pattern — the recurrence dp[i] = max(dp[i-1], dp[i-2] + nums[i])
appears (with small variations) in House Robber II (circular
street), Delete and Earn, and other "can't pick two neighbors"
problems. Once you recognize this recurrence shape, a whole
family of problems becomes solvable the same way.
"""
