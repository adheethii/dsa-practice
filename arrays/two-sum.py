"""
Problem: Two Sum
Difficulty: Easy
Category: Arrays
LeetCode: #1

Problem Statement:
Given an array of integers nums and an integer target,
return indices of the two numbers that add up to target.
You may assume each input has exactly one solution.
You may not use the same element twice.

Example:
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  (because nums[0] + nums[1] = 2 + 7 = 9)
"""

# ─────────────────────────────────────────────
# APPROACH 1: Brute Force
# Time: O(n²) | Space: O(1)
# ─────────────────────────────────────────────

def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# ─────────────────────────────────────────────
# APPROACH 2: HashMap (Optimal)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def two_sum(nums, target):
    """
    Key insight:
    For each number, we need (target - number).
    Store each number's index in a hashmap.
    Check if complement exists in hashmap.

    Example walkthrough:
    nums = [2, 7, 11, 15], target = 9

    i=0: num=2, complement=7, seen={} → not found → seen={2:0}
    i=1: num=7, complement=2, seen={2:0} → FOUND at index 0!
    return [0, 1] ✅
    """
    seen = {}   # {number: index}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []   # no solution found


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test 2
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test 3
    assert two_sum([3, 3], 6) == [0, 1]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Brute Force:
- Time: O(n²) — nested loops
- Space: O(1) — no extra space

HashMap (Optimal):
- Time: O(n) — single pass through array
- Space: O(n) — hashmap stores up to n elements

Trade-off: We use extra space to gain speed.

KEY PATTERN LEARNED:
When you need to find a pair that satisfies a condition,
use a HashMap to store what you've seen.
"For each element, what do I need?" → check if it exists.
"""
