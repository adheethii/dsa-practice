"""
Problem: Product of Array Except Self
Difficulty: Medium
Category: Arrays
LeetCode: #238

Problem Statement:
Given an array nums, return an array where answer[i] is the
product of all elements except nums[i].
You must NOT use division, and solve in O(n) time.

Example:
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Explanation:
answer[0] = 2*3*4 = 24
answer[1] = 1*3*4 = 12
answer[2] = 1*2*4 = 8
answer[3] = 1*2*3 = 6
"""

# ─────────────────────────────────────────────
# APPROACH: Prefix and Suffix Products (Optimal)
# Time: O(n) | Space: O(1) extra (excluding output array)
# ─────────────────────────────────────────────

def product_except_self(nums):
    """
    Key insight:
    answer[i] = (product of everything BEFORE i) * (product of everything AFTER i)

    Do this in TWO passes:
    1. Left to right: store product of all elements BEFORE i
    2. Right to left: multiply by product of all elements AFTER i

    Example walkthrough:
    nums = [1, 2, 3, 4]

    Pass 1 (prefix products):
    answer[0] = 1           (nothing before index 0)
    answer[1] = 1           (product before index 1: just nums[0]=1)
    answer[2] = 1*2 = 2     (product before index 2: nums[0]*nums[1])
    answer[3] = 1*2*3 = 6   (product before index 3)
    → answer = [1, 1, 2, 6]

    Pass 2 (suffix products, multiply in):
    right = 1
    i=3: answer[3] = 6 * 1 = 6,  right = 1*4 = 4
    i=2: answer[2] = 2 * 4 = 8,  right = 4*3 = 12
    i=1: answer[1] = 1 * 12 = 12, right = 12*2 = 24
    i=0: answer[0] = 1 * 24 = 24, right = 24*1 = 24

    Final: [24, 12, 8, 6] ✅
    """
    n = len(nums)
    answer = [1] * n

    # Pass 1: prefix products (product of everything to the LEFT)
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Pass 2: suffix products (product of everything to the RIGHT)
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Prefix/Suffix Approach:
- Time:  O(n) — two passes through array
- Space: O(1) — excluding output array (which is required)

KEY PATTERN LEARNED:
When you need "everything except current position", think
prefix + suffix products/sums. Calculate running product
from left, then running product from right, combine them.
Avoids division entirely — works even with zeros in the array!
"""
