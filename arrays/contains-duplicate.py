"""
Problem: Contains Duplicate
Difficulty: Easy
Category: Arrays
LeetCode: #217

Problem Statement:
Given an integer array nums, return true if any value appears
at least twice in the array, and false if every element is distinct.

Example:
Input:  nums = [1, 2, 3, 1]
Output: True

Input:  nums = [1, 2, 3, 4]
Output: False
"""

# ─────────────────────────────────────────────
# APPROACH 1: Sorting
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────

def contains_duplicate_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


# ─────────────────────────────────────────────
# APPROACH 2: HashSet (Optimal)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def contains_duplicate(nums):
    """
    Key insight:
    Use a set to track seen numbers.
    If a number is already in the set → duplicate found!

    Example walkthrough:
    nums = [1, 2, 3, 1]

    num=1 → seen={} → not in seen → seen={1}
    num=2 → seen={1} → not in seen → seen={1,2}
    num=3 → seen={1,2} → not in seen → seen={1,2,3}
    num=1 → seen={1,2,3} → IN SEEN! → return True ✅
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# One-liner version
def contains_duplicate_oneliner(nums):
    return len(nums) != len(set(nums))


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert contains_duplicate([]) == False
    assert contains_duplicate([1]) == False

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Sorting:
- Time:  O(n log n)
- Space: O(1)

HashSet (Optimal):
- Time:  O(n) — single pass
- Space: O(n) — set stores up to n elements

KEY PATTERN LEARNED:
When checking for duplicates → use a HashSet.
Set lookup is O(1) average.
One-liner: len(nums) != len(set(nums)) works but
HashSet approach is better for early exit on large arrays.
"""
