"""
Problem: Permutations
Difficulty: Medium
Category: Backtracking
LeetCode: #46

Problem Statement:
Given an array of distinct integers, return ALL possible
permutations (arrangements) of the elements.

Example:
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# ─────────────────────────────────────────────
# APPROACH: Backtracking with a "used" tracker
# Time: O(n * n!) | Space: O(n) recursion depth
# ─────────────────────────────────────────────

def permute(nums):
    """
    Key insight:
    Build each permutation one element at a time. At each step,
    try adding EVERY number not already used in the current path.
    When the path reaches full length, record it and backtrack
    (remove the last number, try a different one).

    Example walkthrough (partial):
    nums = [1,2,3]

    path=[], try 1 → path=[1]
      try 2 → path=[1,2]
        try 3 → path=[1,2,3], length==3 → RECORD [1,2,3]
        backtrack → path=[1,2]
      backtrack → path=[1]
      try 3 → path=[1,3]
        try 2 → path=[1,3,2], length==3 → RECORD [1,3,2]
        backtrack
      backtrack → path=[]
    try 2 → ...(continues similarly for all 6 permutations)
    """
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])   # copy the completed permutation
            return

        for i in range(len(nums)):
            if used[i]:
                continue   # skip numbers already in the current path

            used[i] = True
            path.append(nums[i])

            backtrack(path, used)

            # Undo — backtrack!
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    result = permute([1,2,3])
    assert len(result) == 6   # 3! = 6 permutations

    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    result_sets = [tuple(p) for p in result]
    expected_sets = [tuple(p) for p in expected]
    assert set(result_sets) == set(expected_sets)

    assert len(permute([0,1])) == 2
    assert permute([1]) == [[1]]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Backtracking:
- Time:  O(n * n!) — n! permutations, each takes O(n) to build/copy
- Space: O(n) — recursion depth equals array length (plus output)

KEY PATTERN LEARNED:
Permutations differ from Combination Sum in one key way: there's
no "start index" restricting which numbers come next — ANY unused
number can be tried at each position, which is exactly why a
separate 'used' boolean array is needed here (Combination Sum
instead used a start index, since order didn't matter there and
reuse was allowed). Recognizing "does order matter, can elements
repeat" is what determines which backtracking template to reach for.
"""
