"""
Problem: Palindrome Partitioning
Difficulty: Medium
Category: Backtracking / Strings
LeetCode: #131

Problem Statement:
Given a string s, partition it such that every substring in the
partition is a palindrome. Return ALL possible palindrome
partitionings.

Example:
Input:  s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""

# ─────────────────────────────────────────────
# APPROACH: Backtracking with Palindrome Check
# Time: O(n * 2^n) worst case | Space: O(n) recursion depth
# ─────────────────────────────────────────────

def partition(s):
    """
    Key insight:
    At each position, try every possible "next cut point" — but
    ONLY continue down that path if the substring formed IS a
    palindrome. This prunes the search tree early instead of
    generating every possible partition and checking afterward.

    Example walkthrough:
    s = "aab"

    start=0, path=[]
      try "a" (s[0:1]) → is palindrome? yes → path=["a"]
        start=1
        try "a" (s[1:2]) → is palindrome? yes → path=["a","a"]
          start=2
          try "b" (s[2:3]) → is palindrome? yes → path=["a","a","b"]
            start=3 == len(s) → RECORD ["a","a","b"]
          backtrack
        backtrack → path=["a"]
        try "ab" (s[1:3]) → is palindrome? NO ("ab" != "ba") → skip
      backtrack → path=[]
      try "aa" (s[0:2]) → is palindrome? yes → path=["aa"]
        start=2
        try "b" (s[2:3]) → is palindrome? yes → path=["aa","b"]
          start=3 == len(s) → RECORD ["aa","b"]
    """
    result = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])   # reached the end — valid full partition
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]

            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)   # continue partitioning from where we cut
                path.pop()             # undo — backtrack!
            # If not a palindrome, simply don't recurse — this IS the pruning

    backtrack(0, [])
    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    result = partition("aab")
    result_sets = [tuple(p) for p in result]
    assert ("a", "a", "b") in result_sets
    assert ("aa", "b") in result_sets
    assert len(result) == 2

    assert partition("a") == [["a"]]

    result2 = partition("aabb")
    # Every returned partition must consist ENTIRELY of palindromes
    for part in result2:
        for piece in part:
            assert piece == piece[::-1]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Backtracking with pruning:
- Time:  O(n * 2^n) worst case — there are up to 2^(n-1) ways to
         partition a string of length n, and each partition takes
         O(n) to build; palindrome checks add further cost per call
- Space: O(n) — recursion depth, plus output storage

KEY PATTERN LEARNED:
This combines two ideas already seen separately: the "try every
cut point going forward" shape from Subsets (using a start index),
PLUS a validity check (is_palindrome) that PRUNES invalid branches
before recursing further — rather than generating everything and
filtering afterward. Checking validity BEFORE recursing, not after,
is what keeps this efficient for longer strings.
"""
