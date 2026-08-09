""" 
Problem: Subsets 
Difficulty: Medium
Category: Backtracking
LeetCode: #78

Problem Statement:
Given an array of unique integers, return ALL possible subsets
(the power set), including the empty set and the full set itself.

Example:
Input:  nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
(order may vary)
"""

# ─────────────────────────────────────────────
# APPROACH: Backtracking — Include/Exclude Decision Tree
# Time: O(n * 2^n) | Space: O(n) recursion depth
# ─────────────────────────────────────────────

def subsets(nums):
    """
    Key insight:
    Unlike Permutations, EVERY partial path here is a valid
    subset — we don't wait until the path reaches full length.
    At each element, there's a binary choice: include it in
    the current subset, or don't. This naturally explores all
    2^n combinations.

    Example walkthrough:
    nums = [1,2,3]

    start=0, path=[] → RECORD [] (every path recorded immediately)
      i=0: include 1 → path=[1] → RECORD [1]
        i=1: include 2 → path=[1,2] → RECORD [1,2]
          i=2: include 3 → path=[1,2,3] → RECORD [1,2,3]
          backtrack → path=[1,2]
        backtrack → path=[1]
        i=2: include 3 → path=[1,3] → RECORD [1,3]
        backtrack → path=[1]
      backtrack → path=[]
      i=1: include 2 → path=[2] → RECORD [2]
      ...continues for all remaining combinations
    """
    result = []

    def backtrack(start, path):
        result.append(path[:])   # every path IS a valid subset — record immediately

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)   # move forward, never revisit earlier indices
            path.pop()               # undo — backtrack!

    backtrack(0, [])
    return result


# ─────────────────────────────────────────────
# ALTERNATIVE: Iterative (build up subsets by doubling)
# ─────────────────────────────────────────────

def subsets_iterative(nums):
    """
    Start with just the empty set. For each number, take every
    EXISTING subset and create a new copy WITH that number added.
    This doubles the subset count at each step — exactly 2^n total.
    """
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    result = subsets([1,2,3])
    assert len(result) == 8   # 2^3 = 8 subsets

    result_sets = {tuple(sorted(s)) for s in result}
    expected_sets = {(), (1,), (2,), (1,2), (3,), (1,3), (2,3), (1,2,3)}
    assert result_sets == expected_sets

    assert len(subsets([0])) == 2
    assert len(subsets_iterative([1,2,3])) == 8

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Backtracking:
- Time:  O(n * 2^n) — 2^n subsets total, each takes O(n) to copy
- Space: O(n) — recursion depth (plus output storage)

KEY PATTERN LEARNED:
The core difference from Permutations: here, EVERY node in the
recursion tree is a valid answer (record immediately on entry),
not just the leaves. And using 'start' index instead of a 'used'
array is correct here because order doesn't matter for subsets —
[1,2] and [2,1] would be the same subset, so we only ever move
forward through indices, never back to reconsider earlier ones.
"""
