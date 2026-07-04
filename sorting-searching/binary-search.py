"""
Problem: Binary Search
Difficulty: Easy
Category: Sorting & Searching
LeetCode: #704

Problem Statement:
Given a sorted array of integers nums and an integer target,
return the index of target. If not found, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example:
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4  (nums[4] = 9)

Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1  (not found)
"""

# ─────────────────────────────────────────────
# APPROACH: Binary Search (Iterative)
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────

def binary_search(nums, target):
    """
    Key insight:
    Array is sorted → we can eliminate half the search space each step.
    Keep two pointers (left, right) and check the middle element.

    Example walkthrough:
    nums = [-1, 0, 3, 5, 9, 12], target = 9

    left=0, right=5, mid=2 → nums[2]=3 < 9 → search right half
    left=3, right=5, mid=4 → nums[4]=9 == 9 → FOUND! return 4 ✅
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1      # target in right half
        else:
            right = mid - 1     # target in left half

    return -1   # not found


# ─────────────────────────────────────────────
# APPROACH 2: Recursive
# Time: O(log n) | Space: O(log n) — call stack
# ─────────────────────────────────────────────

def binary_search_recursive(nums, target, left=0, right=None):
    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1 — found
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

    # Test 2 — not found
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Test 3 — single element found
    assert binary_search([5], 5) == 0

    # Test 4 — single element not found
    assert binary_search([5], 3) == -1

    # Test 5 — first element
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

    # Test 6 — last element
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Iterative:
- Time:  O(log n) — halve search space each iteration
- Space: O(1) — only two pointers

Recursive:
- Time:  O(log n) — same logic
- Space: O(log n) — recursive call stack

KEY PATTERN LEARNED:
Binary search works on SORTED arrays.
Always calculate mid = (left + right) // 2
Three cases: found / go right / go left
Template: while left <= right → check mid → update left or right
"""
