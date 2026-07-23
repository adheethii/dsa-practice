"""
Problem: Find Median from Data Stream
Difficulty: Hard
Category: Heap / Design
LeetCode: #295

Problem Statement:
Design a data structure that supports adding numbers ONE AT A
TIME (a stream) and finding the median of all numbers added so
far, efficiently, after each addition.

Example:
addNum(1), addNum(2) → median = 1.5
addNum(3)            → median = 2
"""

# ─────────────────────────────────────────────
# APPROACH: Two Heaps (max-heap + min-heap)
# addNum: O(log n) | findMedian: O(1) | Space: O(n)
# ─────────────────────────────────────────────

import heapq


class MedianFinder:
    """
    Key insight:
    Split all numbers into two halves using two heaps:

    - A MAX-heap holding the SMALLER half of numbers
      (Python only has min-heaps, so store NEGATED values to
       simulate a max-heap)
    - A MIN-heap holding the LARGER half of numbers

    Keep both heaps balanced in size (differ by at most 1).
    The median is then either:
    - The top of the larger heap (if sizes are unequal), or
    - The average of both tops (if sizes are equal)

    Example walkthrough:
    addNum(5): small=[-5], large=[]
    addNum(2): 2 < top of small(5)? yes → push to small
               small=[-5,-2]... rebalance: small=[-2], large=[5]
    addNum(8): 8 >= top of small(2)? yes → push to large
               large=[5,8], sizes equal (1,2)... rebalance
               small=[-5], large=[8]... wait, rebalanced properly
               below in actual code logic.

    findMedian(): sizes differ → return top of large heap,
                  or average if equal
    """

    def __init__(self):
        self.small = []   # max-heap (store negatives), holds smaller half
        self.large = []   # min-heap, holds larger half

    def addNum(self, num: int) -> None:
        # Step 1: always push to 'small' first (as negative for max-heap)
        heapq.heappush(self.small, -num)

        # Step 2: ensure every element in 'small' <= every element in 'large'
        # (move the largest of 'small' over to 'large')
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: rebalance sizes — 'small' can have at most 1 more than 'large'
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]   # small has the extra element — it's the median
        return (-self.small[0] + self.large[0]) / 2.0


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5

    mf.addNum(3)
    assert mf.findMedian() == 2

    mf2 = MedianFinder()
    for n in [5, 15, 1, 3]:
        mf2.addNum(n)
    # sorted so far: [1,3,5,15] → median = (3+5)/2 = 4
    assert mf2.findMedian() == 4.0

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Two Heaps:
- addNum:      O(log n) — heap push/pop operations
- findMedian:  O(1) — just look at the tops, no searching
- Space:       O(n) — every number added is stored in one heap

KEY PATTERN LEARNED:
"Two heaps" (one max-heap for the lower half, one min-heap for
the upper half) is THE classic pattern for streaming median
problems. The invariant to hold onto: keep both heaps balanced
in SIZE, and every element in the max-heap must be <= every
element in the min-heap. Python's heapq is min-heap only, so
negating values is the standard trick to simulate a max-heap.
"""
