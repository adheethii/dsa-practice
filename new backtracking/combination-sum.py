"""
Problem: Combination Sum
Difficulty: Medium
Category: Backtracking
LeetCode: #39

Problem Statement:
Given an array of distinct integers candidates and a target,
return all unique combinations where the chosen numbers sum
to target. The same number may be used unlimited times.

Example:
Input:  candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""

# ─────────────────────────────────────────────
# APPROACH: Backtracking
# Time: O(2^target) worst case | Space: O(target)
# ─────────────────────────────────────────────

def combination_sum(candidates, target):
    """
    Key insight:
    At each step, either INCLUDE the current candidate (and stay
    at the same index, since it can be reused) or MOVE ON to the
    next candidate. Backtrack when sum exceeds target or we run
    out of candidates.

    Example walkthrough (partial):
    candidates=[2,3,6,7], target=7

    start=0, path=[], remaining=7
      include 2: path=[2], remaining=5
        include 2: path=[2,2], remaining=3
          include 2: path=[2,2,2], remaining=1 → too small, backtrack
          include 3: path=[2,2,3], remaining=0 → FOUND! [2,2,3]
        move to 3: path=[2], remaining=5, start=1...
    """
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])   # copy the current path
            return
        if remaining < 0:
            return   # overshot — dead end

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            # Pass i (not i+1) — same number can be reused
            backtrack(i, path, remaining - candidates[i])
            path.pop()   # undo — backtrack!

    backtrack(0, [], target)
    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    result = combination_sum([2,3,6,7], 7)
    result_sets = [sorted(r) for r in result]
    assert sorted([2,2,3]) in result_sets
    assert sorted([7]) in result_sets

    result2 = combination_sum([2,3,5], 8)
    assert len(result2) == 3   # [2,2,2,2],[2,3,3],[3,5]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Backtracking:
- Time:  O(2^target) worst case — many branching possibilities
- Space: O(target) — max recursion depth

KEY PATTERN LEARNED:
When a number can be REUSED, pass the same start index (not
start+1) on the recursive call — this is the key difference
from Combination Sum II (no reuse) or Permutations (all reused,
no start index needed at all). Always append/pop for the path
to properly backtrack.
"""
