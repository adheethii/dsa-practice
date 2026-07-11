"""
Problem: Majority Element
Difficulty: Easy
Category: Arrays
LeetCode: #169

Problem Statement:
Given an array nums of size n, return the majority element —
the element that appears more than ⌊n/2⌋ times.
You may assume the majority element always exists.

Example:
Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2  (appears 4 times, n=7, majority needs >3)
"""

# ─────────────────────────────────────────────
# APPROACH 1: HashMap Counting
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def majority_element_hashmap(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num


# ─────────────────────────────────────────────
# APPROACH 2: Boyer-Moore Voting Algorithm (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def majority_element(nums):
    """
    Key insight (Boyer-Moore Voting):
    Think of it as a "battle" — majority element cancels out
    minority elements. Since majority appears >n/2 times,
    it will always "win" in the end.

    Example walkthrough:
    nums = [2, 2, 1, 1, 1, 2, 2]

    candidate=2, count=1
    num=2: same as candidate → count=2
    num=1: different → count=1
    num=1: different → count=0
    num=1: count=0 → candidate=1, count=1
    num=2: different → count=0
    num=2: count=0 → candidate=2, count=1

    Final candidate = 2 ✅
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element([1]) == 1
    assert majority_element([1, 1, 2]) == 1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Boyer-Moore Voting:
- Time:  O(n) — single pass
- Space: O(1) — only two variables

KEY PATTERN LEARNED:
Boyer-Moore Voting Algorithm is a clever O(1) space trick
for majority element problems. The intuition: pair up
different elements to "cancel out" — majority always survives.
This ONLY works when majority element is guaranteed to exist.
"""
