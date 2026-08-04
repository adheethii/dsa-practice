"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Category: Binary Search
LeetCode: #33
  
Problem Statement:
A sorted array is rotated at some unknown pivot (e.g. [4,5,6,7,0,1,2]
was [0,1,2,4,5,6,7] rotated). Given the rotated array and a target,
return its index, or -1 if not found. Must run in O(log n).

Example:
Input:  nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

# ─────────────────────────────────────────────
# APPROACH: Modified Binary Search
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────

def search(nums, target):
    """
    Key insight:
    At any mid point, AT LEAST ONE HALF of the array (left or
    right of mid) is guaranteed to be normally sorted, even
    though the whole array isn't. Figure out which half is
    sorted, then check if target falls within that half's range
    to decide which side to continue searching.

    Example walkthrough:
    nums = [4,5,6,7,0,1,2], target = 0

    left=0, right=6, mid=3 (val=7)
    Is left half [4,5,6,7] sorted? nums[left]=4 <= nums[mid]=7 → yes
    Is target(0) in range [4,7]? No → search right half
    left=4, right=6, mid=5 (val=1)
    Is left half [0,1] sorted? nums[left]=0 <= nums[mid]=1 → yes
    Is target(0) in range [0,1]? Yes → search left half
    left=4, right=4, mid=4 (val=0) → FOUND, return 4 ✅
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is normally sorted
        if nums[left] <= nums[mid]:
            # Left half [left..mid] is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1   # target is in the sorted left half
            else:
                left = mid + 1    # target must be in the right half
        else:
            # Right half [mid..right] is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1    # target is in the sorted right half
            else:
                right = mid - 1   # target must be in the left half

    return -1


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert search([4,5,6,7,0,1,2], 0) == 4
    assert search([4,5,6,7,0,1,2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([5,1,3], 5) == 0
    assert search([3,1], 1) == 1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Modified Binary Search:
- Time:  O(log n) — still halves the search space each step
- Space: O(1) — just three pointers

KEY PATTERN LEARNED:
For "rotated sorted array" problems, the rotation doesn't break
binary search — it just means you must first figure out WHICH
half is sorted (compare nums[left] to nums[mid]) before deciding
whether the target could be in that sorted half's value range.
This exact technique extends to: Find Minimum in Rotated Sorted
Array, Search in Rotated Sorted Array II (with duplicates).
"""
