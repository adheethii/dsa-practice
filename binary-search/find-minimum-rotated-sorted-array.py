"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Category: Binary Search
LeetCode: #153

Problem Statement:
A sorted array with distinct values is rotated at an unknown
pivot. Find the minimum element, in O(log n) time.

Example:
Input:  nums = [4,5,6,7,0,1,2]
Output: 0
"""

# ─────────────────────────────────────────────
# APPROACH: Binary Search on the Rotation Point
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────

def find_min(nums):
    """
    Key insight:
    The minimum is exactly the ROTATION POINT — the one place
    where the normal ascending order "breaks". Compare the
    middle element to the RIGHTMOST element to decide which
    half the break is in:

    - If nums[mid] > nums[right]: the break (and therefore the
      minimum) is somewhere in the RIGHT half, so move left = mid+1
    - If nums[mid] <= nums[right]: the right half is already
      sorted, so the minimum is at mid or somewhere in the LEFT
      half, so move right = mid (not mid-1, mid could BE the answer)

    Example walkthrough:
    nums = [4,5,6,7,0,1,2]

    left=0, right=6, mid=3 (val=7)
    nums[mid]=7 > nums[right]=2 → break is in right half
    left=4, right=6, mid=5 (val=1)
    nums[mid]=1 <= nums[right]=2 → break is at mid or left half
    right=5
    left=4, right=5, mid=4 (val=0)
    nums[mid]=0 <= nums[right]=1 → break is at mid or left half
    right=4
    left=4, right=4 → loop ends, return nums[4]=0 ✅
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum must be to the right of mid
            left = mid + 1
        else:
            # Minimum is at mid or to the left of it
            right = mid

    return nums[left]   # left == right at this point, pointing at the minimum


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert find_min([4,5,6,7,0,1,2]) == 0
    assert find_min([3,4,5,1,2]) == 1
    assert find_min([11,13,15,17]) == 11   # not rotated at all
    assert find_min([1]) == 1
    assert find_min([2,1]) == 1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Binary Search on Rotation Point:
- Time:  O(log n) — halves the search space each iteration
- Space: O(1) — two pointers only

KEY PATTERN LEARNED:
This is the cleaner sibling of Search in Rotated Sorted Array —
here we're finding the rotation point ITSELF rather than an
arbitrary target. Comparing nums[mid] to nums[right] (not
nums[left]) is the key trick — it correctly narrows toward the
one place where ascending order breaks, converging left and
right onto the minimum.
"""
