"""
Problem: Maximum Subarray
Difficulty: Medium
Category: Arrays / Dynamic Programming
LeetCode: #53

Problem Statement:
Given an integer array nums, find the subarray with the largest sum
and return its sum.

Example:
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6  (subarray [4, -1, 2, 1] has the largest sum = 6)

Input:  nums = [1]
Output: 1

Input:  nums = [5, 4, -1, 7, 8]
Output: 23
"""

# ─────────────────────────────────────────────
# APPROACH: Kadane's Algorithm
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def max_subarray(nums):
    """
    Key insight (Kadane's Algorithm):
    At each position, decide:
    - Extend the current subarray (current_sum + num)
    - Start a new subarray from here (num alone)
    Pick whichever is larger.

    Example walkthrough:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    num=-2: current=-2, max_sum=-2
    num=1:  current=max(1, -2+1)=1,  max_sum=1
    num=-3: current=max(-3, 1-3)=-2, max_sum=1
    num=4:  current=max(4, -2+4)=4,  max_sum=4
    num=-1: current=max(-1, 4-1)=3,  max_sum=4
    num=2:  current=max(2, 3+2)=5,   max_sum=5
    num=1:  current=max(1, 5+1)=6,   max_sum=6 ✅
    num=-5: current=max(-5, 6-5)=1,  max_sum=6
    num=4:  current=max(4, 1+4)=5,   max_sum=6
    """
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1]) == -1
    assert max_subarray([-2, -1]) == -1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Kadane's Algorithm:
- Time:  O(n) — single pass
- Space: O(1) — only two variables

KEY PATTERN LEARNED:
Kadane's algorithm is a classic DP pattern.
At each step: should I extend current subarray or start fresh?
current = max(num, current + num)
This is one of the most famous interview problems — memorise the pattern!
"""
