"""
Problem: Merge Intervals
Difficulty: Medium
Category: Arrays / Sorting
LeetCode: #56

Problem Statement:
Given an array of intervals, merge all overlapping intervals
and return the resulting non-overlapping intervals.

Example:
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: [1,3] and [2,6] overlap, merge into [1,6]
"""

# ─────────────────────────────────────────────
# APPROACH: Sort then Merge
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────

def merge(intervals):
    """
    Key insight:
    Sort intervals by start time first. Then, going through
    in order, we only need to check if the CURRENT interval
    overlaps with the LAST merged interval so far.

    Example walkthrough:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    (already sorted by start)

    result = [[1,3]]
    next [2,6]: 2 <= 3 (last end)? YES → merge → result=[[1,6]]
    next [8,10]: 8 <= 6? NO → new interval → result=[[1,6],[8,10]]
    next [15,18]: 15 <= 10? NO → new interval → result=[[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            # Overlap — merge by extending the end time
            last[1] = max(last[1], current[1])
        else:
            # No overlap — add as new interval
            merged.append(current)

    return merged


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([[1,4],[0,4]]) == [[0,4]]
    assert merge([[1,4]]) == [[1,4]]
    assert merge([]) == []

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Sort then Merge:
- Time:  O(n log n) — dominated by the sort
- Space: O(n) — for the merged result (or O(log n) if sort is in-place)

KEY PATTERN LEARNED:
For interval problems, ALWAYS sort by start time first.
Once sorted, you only ever need to compare against the LAST
merged interval — not all previous ones. This pattern extends to:
Insert Interval, Meeting Rooms, Non-overlapping Intervals.
"""
