"""
Problem: Container With Most Water
Difficulty: Medium
Category: Arrays / Two Pointers
LeetCode: #11

Problem Statement:
Given n non-negative integers representing heights of vertical
lines, find two lines that together with the x-axis form a
container that holds the most water. Return the max area.

Example:
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49  (lines at index 1 (height=8) and index 8 (height=7):
             width=7, height=min(8,7)=7, area=49)
"""

# ─────────────────────────────────────────────
# APPROACH: Two Pointers (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def max_area(height):
    """
    Key insight:
    Start with the WIDEST possible container (pointers at both
    ends). Area = width * min(left_height, right_height).

    To maximize area, we should move the pointer at the SHORTER
    line inward — moving the taller one can only decrease width
    without any chance of increasing the limiting (shorter) height.

    Example walkthrough:
    height = [1,8,6,2,5,4,8,3,7]

    left=0(h=1), right=8(h=7): area=8*min(1,7)=8, max=8
      1 < 7, move left (shorter side)
    left=1(h=8), right=8(h=7): area=7*min(8,7)=49, max=49
      7 < 8, move right (shorter side)
    left=1(h=8), right=7(h=3): area=6*min(8,3)=18, max=49
      3 < 8, move right
    ...continues, but 49 remains the max
    """
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_water = max(max_water, current_area)

        # Move the pointer at the SHORTER line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert max_area([1,1]) == 1
    assert max_area([4,3,2,1,4]) == 16
    assert max_area([1,2,1]) == 2

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Two Pointers:
- Time:  O(n) — each pointer moves at most n times total
- Space: O(1) — only two pointers and a running max

KEY PATTERN LEARNED:
When maximizing area/volume bounded by two "walls", start wide
and greedily move the pointer at the SHORTER wall inward — this
is provably safe because moving the taller wall can never help
(width decreases, and the limiting height can't improve). This
greedy two-pointer pattern is easy to mis-justify — the proof
(moving the taller side is always suboptimal) is worth being
able to explain clearly in an interview, not just recite.
"""
